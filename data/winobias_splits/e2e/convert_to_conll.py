"""
convert the uw predictions to the conll format.
python conver_to_conll.py input_path predictions_path  output_path
"""
import json
import sys

for i in range(395):
    conll_test_key_filename = sys.argv[1] + str(i) +'.v4_auto_conll'
    uw_system_out_filename = sys.argv[2] + str(i) + '.jsonlines'
    out_file = sys.argv[3] + str(i) + '-uw_coref_system_output.txt'

    doc_dict = {}
    for line in open(uw_system_out_filename, "r"):
        dictionary = json.loads(line)
        doc_key_tokens = dictionary['doc_key'].split('_')

        doc_key = '_'.join(doc_key_tokens[:-1])
        part_id = int(doc_key_tokens[-1])
        doc_dict[(doc_key, part_id)] = dictionary['predicted_clusters']

    print(len(doc_dict))

    fw = open(out_file, 'w', encoding="utf8")

    doc_key = None
    part_id = None
    current_mention_starts = None
    current_mention_ends = None
    word_no = 0
    cluster_id = 0

    for line in open(conll_test_key_filename, 'r', encoding="utf8"):
        line = line.strip()
        if '#begin document' in line:
            doc_key = line[line.find("(")+1:line.find(")")]
            part_id = int(line.split('part')[1].strip())
            current_mention_starts = {}
            current_mention_ends = {}

            for cluster in doc_dict[(doc_key, part_id)]:
                cluster_id += 1
                for mention in cluster:
                    if mention[0] in current_mention_starts:
                        current_mention_starts[mention[0]].append(cluster_id)
                    else:
                        current_mention_starts[mention[0]] = [cluster_id]

                    if mention[1] in current_mention_ends:
                        current_mention_ends[mention[1]].append(cluster_id)
                    else:
                        current_mention_ends[mention[1]] = [cluster_id]
            fw.write(line + '\n')
        elif '#end document' in line:
            fw.write(line + '\n')
            word_no = 0
        elif not line:
            fw.write('\n')
        else:
            tokens = line.split()
            label_dict = {}
            if word_no in current_mention_starts:
                for cluster_num in current_mention_starts[word_no]:
                    if cluster_num in label_dict:
                        label_dict[cluster_num].append(-1)
                    else:
                        label_dict[cluster_num] = [-1]
            if word_no in current_mention_ends:
                for cluster_num in current_mention_ends[word_no]:
                    if cluster_num in label_dict:
                        label_dict[cluster_num].append(1)
                    else:
                        label_dict[cluster_num] = [1]

            label = ''
            for key, value in label_dict.items():
                v = {i: value.count(i) for i in value}
                total_start, total_end = 0, 0
                if -1 in v:
                    total_start = v[-1]
                if 1 in v:
                    total_end = v[1]

                if total_start > total_end:
                    diff = total_start - total_end
                    for j in range(diff):
                        if label:
                            label += '|' + '(' + str(key)
                        else:
                            label += '(' + str(key)

                    if total_start-diff > 0:
                        for j in range(total_start-diff):
                            if label:
                                label += '|' + '(' + str(key) + ')'
                            else:
                                label += '(' + str(key) + ')'
                elif total_start < total_end:
                    diff =  total_end - total_start
                    for j in range(diff):
                        if label:
                            label += '|' + str(key) + ')'
                        else:
                            label += str(key) + ')'

                    if total_end-diff > 0:
                        for j in range(total_end-diff):
                            if label:
                                label += '|' + '(' + str(key) + ')'
                            else:
                                label += '(' + str(key) + ')'
                else:
                    for j in range(total_start):
                        if label:
                            label += '|' + '(' + str(key) + ')'
                        else:
                            label += '(' + str(key) + ')'

            if not label:
                label = '-'

            fw.write('\t'.join(tokens[:-1]) + '\t' + label + '\n')
            word_no += 1

    fw.close()


