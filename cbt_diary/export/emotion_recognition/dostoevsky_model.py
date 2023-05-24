from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

tokenizer = RegexTokenizer()

sentiment_analysis_model = FastTextSocialNetworkModel(tokenizer=tokenizer)

messages = [
    'Я напортачил с задачей на работе Все вокруг ненавидят меня за это',
    'я люблю тебя!!',
    'малолетние дебилы'
]

results = sentiment_analysis_model.predict(messages, k=5)
for message, sentiment in zip(messages, results):
    # привет -> {'speech': 1.0000100135803223, 'skip': 0.0020607432816177607}
    # люблю тебя!! -> {'positive': 0.9886782765388489, 'skip': 0.005394937004894018}
    # малолетние дебилы -> {'negative': 0.9525841474533081, 'neutral': 0.13661839067935944}]
    print(message, '->', sentiment)