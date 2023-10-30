e.g. Is this IMDB movie review a positive one?
There are keywords that can be used to determine the attitute on a movie.

## DNN-based NLU
Feed downstream task data to pre-trained language model to fine-tune. Downstream task data should be as similar to deployment data. 

## Tokenizer
> Crucial component of NLP systems. 

NLP systems need a tokenizer to encode texts into numbers in order for NN to perform calculations.

### Word Splitting
#### Method 1: Split
- "convert" and "converts" are considered as different words
- Punctuations make a different word
#### Method 2: separate words and punctuations
Drawback: larger vocab in multilingual tasks.
"This is an example." -> ["This", "is", "an", "example", "." ].

#### Method 3: Character/Byte-level Encoding
Example: CANINE
Vocab size significantly reduced.
"This is an example." -> ["T", "h", "i", ...].
Drawback: need to handle a much longer sequence. 
#### Method 4: subword
- Adopted by popular LMs (BERT, GPT)
- Each pretrained model comes with its own tokenizer

### Two-step Encoding Process
Calling `tokenizer(sentence)` is equivalent to
- `tokens = tokenizer.tokenize(sentence)`
- `tokenizer.convert_tokens_to_ids(tokens)`

## Overview of the Pipeline
Text -> Tokenization into input_ids and attention masks -> pretrained model -> linear classification head -> output.

## BERT
BERT is the encoder part of the transformer.



