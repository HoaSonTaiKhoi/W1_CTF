import torch.nn as nn
import torch

vocab = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}\n")
class BigramLanguageModel(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.embeddings = nn.Embedding(vocab_size, 64)
        self.linear = nn.Linear(64, vocab_size)

    def forward(self, inputs, targets=None):
        embeds = self.embeddings(inputs)
        logits = self.linear(embeds)
        loss = None
        if targets is not None:
            loss = nn.CrossEntropyLoss()(logits.view(-1, logits.size(-1)), targets.view(-1))
        return logits, loss

model = BigramLanguageModel(len(vocab))
PATH = "C:/Code C/Python_Hash/echo-in-the-cosmos/bigram_model.pth"
model.load_state_dict(torch.load(PATH))
model.eval()

flag = [vocab.index('W')]
value=58
while True:
    if value != 91:
        input_data = torch.tensor([value])
        print(input_data)# Add unsqueeze to add batch dimension
        logits, _ = model(input_data)
        result = torch.max(logits, dim=1)  # Use dim=1 to get the maximum value across the vocabulary dimension
        print(result)
        value = int(result.indices)
        print(vocab[value])
        flag.append(value)
    else:
        break

result = "".join([vocab[order] for order in flag])

print(result)