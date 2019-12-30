<<<<<<< HEAD
from fast_bert.prediction import BertClassificationPredictor
from path import Path
import os

MODEL_PATH = ("C:\\Users\\Desktop\\model\\md")
LABEL_PATH = ("C:\\Users\\Desktop\\model\\label")


#print(MODEL_PATH)
#print(LABEL_PATH)

predictor = BertClassificationPredictor(model_path=MODEL_PATH,label_path=LABEL_PATH,multi_label=True,model_type='bert',do_lower_case=False)

print("-------NO---------")

text = "直接 把 肥宅 的 廢萌 黏土人 模型 砸壞 最 快"
print(text)
print(predictor.predict(text))

print("-------1---------")

text = "我 跟 醫生 說 我 想 出國 打工 度假 （ 本身 喜歡 旅遊 ） ， 醫生 評估 最後 是 可以 的 。"
print(text)
print(predictor.predict(text))


print("-------2---------")

text = "展現真正的自己很重要"
print(text)
print(predictor.predict(text))



=======
from fast_bert.prediction import BertClassificationPredictor
from path import Path
import os

MODEL_PATH = ("C:\\Users\\Desktop\\model\\md")
LABEL_PATH = ("C:\\Users\\Desktop\\model\\label")


#print(MODEL_PATH)
#print(LABEL_PATH)

predictor = BertClassificationPredictor(model_path=MODEL_PATH,label_path=LABEL_PATH,multi_label=True,model_type='bert',do_lower_case=False)

print("-------NO---------")

text = "直接 把 肥宅 的 廢萌 黏土人 模型 砸壞 最 快"
print(text)
print(predictor.predict(text))

print("-------1---------")

text = "我 跟 醫生 說 我 想 出國 打工 度假 （ 本身 喜歡 旅遊 ） ， 醫生 評估 最後 是 可以 的 。"
print(text)
print(predictor.predict(text))


print("-------2---------")

text = "展現真正的自己很重要"
print(text)
print(predictor.predict(text))



>>>>>>> first
