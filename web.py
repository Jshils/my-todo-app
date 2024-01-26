import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"] +"\n"
    todos.append(todo)
    functions.write_todos(todos)

    # """st.session_state is like a dictionary with a key and value in this
    # case the key is new_todo and the value entered in the box with be
    # the value for that key"""

todos = functions.get_todos()


"""The order of the widgets makes a difference - they will display and work 
in the order they are placed in the program"""


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your <b>productivity</b>.",
         unsafe_allow_html=True)

# You can add HTML code to this but it is only allowed for the write method not title
# and subheader

for index, todo in enumerate(todos):
    checkbox = st.checkbox(str(index+1) + " " + todo, key=todo)
    if checkbox: # same as if checkbox == True:
        todos.pop(index) # remove the todo with the index number
        functions.write_todos(todos) # update the todos file
        del st.session_state[todo] # del the item from the session_state also
        st.rerun()
        print(checkbox)


    # we are making the key dynamic by assigning the key to the todo list - it will
    # change for each new todo each time the code is run

st.text_input(label="Enter a new todo", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

# """Note that the function add_todo (which is defined above
# is called from the st.text_input function"""
