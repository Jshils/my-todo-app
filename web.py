import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] +"\n"
    todos.append(todo)
    functions.write_todos(todos)

    # """st.session_state is like a dictionary with a key and value in this
    # case the key is new_todo and the value entered in the box with be
    # the value for that key"""

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
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
