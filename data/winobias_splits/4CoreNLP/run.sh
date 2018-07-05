#!/bin/bash
java -Xmx80g -cp stanford-corenlp-models-current.jar:stanford-english-corenlp-models-current.jar:ejml-0.23.jar:* edu.stanford.nlp.dcoref.SieveCoreferenceSystem -props src/edu/stanford/nlp/coref/properties/deterministic-english-conll.properties  -coref.conllOutputPath conlloutput/ -coref.scorer ./reference-coreference-scorers/v8.01/scorer.pl
#-coref.data /zf2/jz4fu/Github/data/conll/ontonote
