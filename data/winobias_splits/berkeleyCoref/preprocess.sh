java -cp berkeleycoref-1.1.jar -Xmx20g edu.berkeley.nlp.coref.preprocess.PreprocessingDriver ++base.conf \
  -execDir src/main/java/edu/berkeley/nlp/coref/ \
  -inputDir $1 \
  -outputDir $2
