import streamlit as st

# 设置网页标题和侧边栏
st.title("我的个人主页")

# 创建侧边栏导航
page = st.sidebar.radio("导航", ["首页", "个人简历", "作品一：个人待办清单管理工具", "机器学习模型"])

# 首页
if page == "首页":
    st.header("欢迎来到我的个人主页")
    st.write("这里是我的个人主页，您可以查看我的简历、管理我的待办清单，或者尝试我的机器学习模型。")
    st.image("https://placehold.co/400x200?text=Personal+Portrait", caption="个人照片")

# 个人简历页面
elif page == "个人简历":
    st.header("个人简历")

    # 个人基本信息
    st.subheader("基本信息")
    st.markdown("**姓名**: 马韬")
    st.markdown("**邮箱**: 1686302958@QQ.com")
    st.markdown("**电话**: 13451958361")

    # 教育背景
    st.subheader("教育背景")
    st.markdown("徐州医科大学 - 智能医学工程 (2022-2026)**")
    st.markdown("主修课程：机器学习、数据挖掘、人工智能、编程语言等")

    # 工作经验
    st.subheader("工作经验")
    st.markdown("""
    **暂无**
    - 负责数据收集、清洗和分析
    - 帮助团队进行数据驱动的决策
    - 使用 Python 开发自动化分析工具
    """)

    # 技能
    st.subheader("技能")
    st.markdown("- Python, R, SQL")
    st.markdown("- 机器学习, 数据分析")
    st.markdown("- 数据可视化 (Matplotlib, Seaborn, Plotly)")
    st.markdown("- Web 开发 (Streamlit, Flask)")

# 待办清单页面
elif page == "待办清单":
    # 这里是待办清单的功能
    st.header("个人待办清单管理工具")

    # 初始化待办事项列表
    if 'todos' not in st.session_state:
        st.session_state.todos = []


    # 添加待办事项
    def add_todo():
        new_todo = st.session_state.new_todo.strip()
        if new_todo:
            st.session_state.todos.append({
                'text': new_todo,
                'completed': False
            })
            st.session_state.new_todo = ''


    # 删除待办事项
    def delete_todo(index):
        del st.session_state.todos[index]


    # 清空所有待办事项
    def clear_todos():
        st.session_state.todos = []


    # 显示待办事项
    def show_todos():
        if not st.session_state.todos:
            st.info("暂无待办事项")
        else:
            for i, todo in enumerate(st.session_state.todos):
                col1, col2 = st.columns([9, 1])
                with col1:
                    if st.checkbox(todo['text'], key=i, value=todo['completed']):
                        st.session_state.todos[i]['completed'] = True
                    else:
                        st.session_state.todos[i]['completed'] = False
                with col2:
                    if st.button("删除", key=f"delete_{i}"):
                        delete_todo(i)
                        break


    # 主界面布局
    left_col, right_col = st.columns(2)

    with left_col:
        st.subheader("添加待办事项")
        st.text_input("输入待办事项", key="new_todo")
        st.button("添加", on_click=add_todo)

    with right_col:
        st.subheader("待办事项列表")
        show_todos()

    # 添加清空所有待办事项的功能
    if st.session_state.todos:
        st.button("清空所有待办事项", on_click=clear_todos)

# 机器学习模型页面
elif page == "机器学习模型":
    st.header("鸢尾花分类预测")

    # 添加超链接到机器学习预测应用
    st.markdown("[点击这里访问我的机器学习模型](https://super-duper-pancake-69pvr4v5gw7gcrjx5-8501.app.github.dev/)")

    # 可以在这里提供一些关于模型的介绍信息
    st.subheader("关于这个模型")
    st.markdown("这是一个用于预测鸢尾花种类的机器学习模型。")
    st.markdown("它使用了随机森林算法，基于花的四个特征（萼片长度、萼片宽度、花瓣长度、花瓣宽度）进行预测。")
    st.markdown("您可以输入花的特征值，点击链接访问应用并查看预测结果。")
