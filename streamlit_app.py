import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 加载鸢尾花数据集
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# 将数据集分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练随机森林分类器
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# 设置网页标题
st.title("鸢尾花分类预测")

# 添加应用描述
st.write("这个应用使用机器学习模型预测鸢尾花的种类。请输入花的特征值进行预测。")

# 创建用户输入界面
st.sidebar.header("输入花的特征值")

sepal_length = st.sidebar.slider("花萼长度（cm）", 4.3, 7.9, 5.4)
sepal_width = st.sidebar.slider("花萼宽度（cm）", 2.0, 4.4, 3.4)
petal_length = st.sidebar.slider("花瓣长度（cm）", 1.0, 6.9, 1.3)
petal_width = st.sidebar.slider("花瓣宽度（cm）", 0.1, 2.5, 0.2)

# 创建特征列表
features = [sepal_length, sepal_width, petal_length, petal_width]

# 显示用户输入的特征值
st.subheader("输入的特征值")
st.write(pd.DataFrame([{
    "花萼长度（cm）": sepal_length,
    "花萼宽度（cm）": sepal_width,
    "花瓣长度（cm）": petal_length,
    "花瓣宽度（cm）": petal_width
}]))

# 添加预测按钮和结果展示
if st.button("预测"):
    # 使用模型进行预测
    prediction = clf.predict([features])
    prediction_proba = clf.predict_proba([features])

    # 显示预测结果
    st.subheader("预测结果")
    st.write(f"预测的鸢尾花种类：{target_names[prediction][0]}")

    # 显示预测概率
    st.subheader("预测概率")
    proba_df = pd.DataFrame({
        "种类": target_names,
        "概率": prediction_proba[0]
    })
    st.bar_chart(proba_df.set_index("种类"))

# 添加模型性能信息（可选）
st.subheader("模型性能")
st.write(f"模型准确率：{clf.score(X_test, y_test):.2f}")

# 添加数据集展示（可选）
if st.checkbox("显示数据集"):
    st.subheader("鸢尾花数据集")
    df = pd.DataFrame(X, columns=feature_names)
    df["target"] = y
    df["target"] = df["target"].map(lambda x: target_names[x])
    st.write(df.head(10))
