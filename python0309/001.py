import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
import functools
from datetime import datetime
from time import clock

from sklearn import metrics
from tools import load_data, load_source, show_source


def log_time(fn):
    @functools.wraps(fn)
    def wrapper():
        start = clock()
        ret = fn()
        end = clock()
        print("{}  use time: {:.3f} s".format(fn.__name__, end - start))
        return ret

    return wrapper


# 加载训练数据
data_x, data_y = load_data("train.txt")

# 加载原始数据
source_data = load_source("train.csv")

# 打印数据长度
print("len", len(data_x), len(data_y))

# 设置测试数据数量
LEN = -1000
# 划分训练数据和测试数据 注： 当前测试中用到测试数据训练集（train.csv）的数据， 而暂时没有用到测试数据集的数据(test.csv)
x_train, y_train = data_x[:LEN], data_y[:LEN]
x_test, y_test = data_x[LEN:], data_y[LEN:]


@log_time
def tran_LinearRegression():
    # 定义45个线性分类器，并训练数据，每个分类器只对两个数字进行识别
    RegressionDict = {}
    for i in range(10):
        for j in range(i + 1, 10):
            regr = LinearRegression()
            RegressionDict["{}-{}".format(i, j)] = regr
            x_train_tmp = np.array([x_train[index] for index, y in enumerate(y_train) if y in [i, j]])
            y_train_tmp = np.array([0 if y == i else 1 for y in y_train if y in [i, j]])
            regr.fit(x_train_tmp, y_train_tmp)

            # 初始化计数器
    ret_counter = []
    for i in range(len(x_test)):
        ret_counter.append({})
        # 预测数据，并把结果放到计数器中
    tmp_dict = {}
    for key, regression in RegressionDict.items():
        a, b = key.split('-')
        y_test_predict = regression.predict(x_test)
        tmp_dict[key] = [a if item <= 0.5 else b for item in y_test_predict]
        for i, item in enumerate(tmp_dict[key]):
            ret_counter[i][item] = ret_counter[i].get(item, 0) + 1

    predict = []
    for i, item in enumerate(y_test):
        predict.append(int(sorted(ret_counter[i].items(), key=lambda x: x[1], reverse=True)[0][0]))

    return predict


print("\nLinearRegression")
predicted = tran_LinearRegression()
print(metrics.classification_report(y_test, predicted))
print("count:", len(y_test), "ok:", sum([1 for item in range(len(y_test)) if y_test[item] == predicted[item]]))

# 其它常用分类器测试
map_predictor = {
    "LogisticRegression": LogisticRegression(),
    "bayes": GaussianNB(),
    "KNN": KNeighborsClassifier(),
    "DecisionTree": DecisionTreeClassifier(),
    "SVC": SVC()
}

for key, model in map_predictor.items():
    start = clock()
    print("start: ", start, key, datetime.utcnow())
    model.fit(x_train, y_train)
    end = clock()
    print("end: ", end, key, datetime.utcnow())
    print("{}  use time: {:.3f} s".format(key, end - start))
    predicted = model.predict(x_test)
    print(metrics.classification_report(y_test, predicted))
    print("count:", len(y_test), "ok:", sum([1 for item in range(len(y_test)) if y_test[item] == predicted[item]]))