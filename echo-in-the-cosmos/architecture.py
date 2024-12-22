import torch.nn as nn
import torch

vocab = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}\n")


class BigramLanguageModel(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.embeddings = nn.Embedding(vocab_size, 64)  # Changed embedding size
        self.linear = nn.Linear(64, vocab_size)  # Added linear layer
    
    def forward(self, inputs, targets=None):
        embeds = self.embeddings(inputs)
        logits = self.linear(embeds)
        loss = None
        if targets is not None:
            loss = nn.CrossEntropyLoss()(logits.view(-1, logits.size(-1)), targets.view(-1))
        return logits, loss

model=BigramLanguageModel(len(vocab))


value = 58 # W
flag = [58]
for i in range (94):
    if (value != 91):
        input_data = torch.tensor(value)
        with torch.no_grad():  # Use torch.no_grad() to disable gradient calculation during inference
            targets = torch.tensor([vocab.index('E'), vocab.index('c'), vocab.index('h'), vocab.index('o')])
            output, _ = model(input_data, targets)  # Assuming your forward method returns both logits and loss
        result = torch.max(output, dim = 0)
        value = int(result.indices)
        print(vocab[value])
        flag.append(vocab[value])
    else:
        break