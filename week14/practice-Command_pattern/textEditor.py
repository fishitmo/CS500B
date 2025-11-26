from abc import ABC , abstractmethod

# Reciver the actual document

class TextEditor:
    
    def __init__(self):
        self.content = ""
        
    def write(self, text):
        self.content +=text
        print(f"Content: '{self.content}'")
        
    def delete(self, length):
        self.content = self.content[:-length]
        print(f"Content: '{self.content}'")
  
# Command Interface

class Command(ABC):
    
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
       pass
         
class WriteCommand(Command):
    def __init__(self, editor: TextEditor, text):
        self.editor = editor
        self.text = text
        
    def execute(self):
        self.editor.write(self.text)
        
    def undo(self):
        self.editor.delete(len(self.text))
        
class EditorInvoker:
    
    def __init__(self):
        self.history = []
        self.redo_stack = []
        
    def execute_command(self, command):
        command.execute()
        self.history.append(command)
        self.redo_stack.clear()  # clear redo when new action
        
    def undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()
            self.redo_stack.append(command)
            
    def redo(self):
        if self.redo_stack:
            command = self.redo_stack.pop()
            command.execute()
            self.history.append(command)
            


def main():
    editor = TextEditor()
    invoker = EditorInvoker()

    invoker.execute_command(WriteCommand(editor, "Hello "))
    invoker.execute_command(WriteCommand(editor, "World"))

    invoker.undo()  # Remove "World"
    invoker.undo()  # Remove "Hello "
    invoker.redo()  # Add back "Hello "
    
if __name__ == "__main__":
    main()
