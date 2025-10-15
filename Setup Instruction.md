# How to Use the Notebooks in This Course

> Excerpt from [Lesson 0: Introduction](Lesson%200/Introduction.ipynb)

To run this notebook, you need an appropriate environment. This section provides a step-by-step guide to installing and running JupyterLab, our recommended editor.

## Setting up Environments

JupyterLab is a web-based interactive development environment for code and data. In this course, we will use JupyterLab to run and interact with our Python code. JupyterLab is a part of the [Anaconda](https://www.anaconda.com/) distribution, which is a popular Python distribution that includes many commonly used scientific packages. The swiftest way to download Anaconda is following [Anaconda's official download page](https://www.anaconda.com/download/success), which skips the account registration step and provides a direct download link.

<img src="Lesson 0/assets/anaconda_download_page.png" alt="Anaconda download page" width="50%" style="display=block; margin:auto"/>

The left button downloads Anaconda, while the right button downloads Miniconda. Anaconda is a full distribution that can take up at least 5 GB of disk space. If your computer has limited storage, consider using Miniconda instead. Miniconda is a minimal distribution that only includes Python, conda, and a few essential utilities. It requires less than 500 MB of space, but you will need to install additional packages manually as needed.

If you have any questions about details, check out the [official tutorial of Anaconda](https://www.anaconda.com/docs/getting-started/getting-started) for reference.

After installing Anaconda, you can see the Anaconda Navigator, which is a graphical user interface for managing your Anaconda environments. Opening the Anaconda Navigator, you can find the JupyterLab application. Click the "Launch" button to launch JupyterLab.

<img src="Lesson 0/assets/anaconda_navigator.png" alt="Anaconda Navigator" width="50%" style="display=block; margin:auto"/>

If you want to use a Python environment other than Anaconda, you may need to install JupyterLab and other dependencies manually. Fortunately, we have provided a minimal dependency list in the `requirements.txt` file. You can install the dependencies by running the following command in the terminal.

```shell
pip install -r requirements.txt
```

After installing the dependencies, you can start JupyterLab by running the following command.

```shell
jupyter lab
```

It will open a browser window and show the JupyterLab interface (usually at <http://localhost:8888/lab>).

## Using JupyterLab

JupyterLab provides a flexible and intuitive user interface for working with notebooks, which is a little bit like [Visual Studio Code](https://code.visualstudio.com/) (VS Code). You can read the [JupyterLab user guide](https://jupyterlab.readthedocs.io/en/stable/user/interface.html) to learn more about JupyterLab's features. Here let's take a brief look at the interface.

<img src="Lesson 0/assets/jupyterlab_interface.png" alt="Interface of JupyterLab" width="50%" style="display=block; margin:auto"/>

- The **menu bar** at the top of JupyterLab has top-level menus that expose actions available in JupyterLab with their keyboard shortcuts.
- The **left sidebar** contains the file browser, kernel monitor, table of contents, and extension manager.
- The **main area** contains the notebook editor, which allows you to write and run code.
- The **right sidebar** contains the metadata inspector and debugger.
- The **status bar** at the bottom of the screen shows the current notebook, kernel, and other information.

### Components of a Notebook

A notebook consists of a series of cells, which are mainly divided into code cells and Markdown cells. To create a cell, you need to select the cell directly above the location where you want to create it. A blue vertical line will appear on the left side of the selected cell. Then, you can click the "+" button in the toolbar to create a new cell below the selected cell.

<img src="Lesson 0/assets/main_insert_below.png" alt="Create cell" width="50%" style="display=block; margin:auto"/>

Code cells are used to write and execute Python code. As we mentioned in Example 1, you can execute a code cell by pressing <kbd>Shift</kbd> + <kbd>Enter</kbd> (or <kbd>Shift</kbd> + <kbd>Return</kbd> on Mac), or clicking the "Run" button in the toolbar.

<img src="Lesson 0/assets/main_run_cell.png" alt="Run cell" width="50%" style="display=block; margin:auto"/>

A code cell may contain the output of the code, which is displayed below the cell. The output can be text, images, or other media. When you select a code cell with output, the blue line on the left side will break at the boundary between the cell and the output.

<img src="Lesson 0/assets/code_cell.png" alt="Code cell output" width="50%" style="display=block; margin:auto"/>

Markdown cells can render rich styles through simple syntax which we will learn later.

<img src="Lesson 0/assets/markdown_cell.png" alt="Markdown cell" width="50%" style="display=block; margin:auto"/>

To edit a Markdown cell, you can double-click the cell into edit mode. If you finished editing, you can "execute" it (remember the shortcut or button) to render the Markdown text.

<img src="Lesson 0/assets/markdown_edit.png" alt="Edit Markdown cell" width="50%" style="display=block; margin:auto"/>

By the way, for any button you are interested in, hover your cursor over it to see a description and the corresponding shortcut (if any). Furthermore, you can change the cell type (code, markdown, or raw text) using the drop-down menu in the toolbar.

<img src="Lesson 0/assets/toolbar_widgets.png" alt="Toolbar widgets" width="50%" style="display=block; margin:auto"/>

When selecting a cell, its upper right corner appears some small widgets. Each corresponds to a cell operation listed below.

| Widget                                                        | Description                          | Default Shortcut                                 |
|---------------------------------------------------------------|--------------------------------------|--------------------------------------------------|
| ![Duplicated cell](Lesson%200/assets/cell_duplicate.png)      | Duplicate the current cell           | None                                             |
| ![Move cell up](Lesson%200/assets/cell_move_up.png)           | Move the current cell up             | <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Up</kbd>   |
| ![Move cell down](Lesson%200/assets/cell_move_down.png)       | Move the current cell down           | <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Down</kbd> |
| ![Insert cell above](Lesson%200/assets/cell_insert_above.png) | Insert a cell above the current cell | <kbd>A</kbd>                                     |
| ![Insert cell below](Lesson%200/assets/cell_insert_below.png) | Insert a cell below the current cell | <kbd>B</kbd>                                     |
| ![Delete cell](Lesson%200/assets/cell_delete.png)             | Delete the current cell              | <kbd>D</kbd>, <kbd>D</kbd> (double press)        |

Besides keyboard shortcuts or buttons, you can also drag and drop the left side of a cell to reorder them. Furthermore, click the left side of cells while pressing <kbd>Shift</kbd> to select multiple cells, and then you can move them together.

### Menu Bar

Now let's take a closer look at the menu bar. The menu bar provides full control over the interface and notebooks. Here are some key features you should know before you start using JupyterLab.

The File menu contains actions for opening and saving notebooks, as well as for creating new notebooks. We can even export our notebook to a variety of formats. Here are some important shortcuts and functionalities:
- <kbd>Ctrl</kbd>+<kbd>S</kbd> is used to save your notebook, although you can enable auto-save in settings.
- <kbd>Alt</kbd>+<kbd>W</kbd> is used to close the current notebook, since <kbd>Ctrl</kbd>+<kbd>W</kbd> is already used on browser to close the current tab.
- The submenu "Save and Export Notebook As" allows you to save your notebook in various formats, including HTML, PDF, and Markdown.
- To create a new notebook, expand the "New" submenu and select "Notebook".

<img src="Lesson 0/assets/menu_file.png" alt="File menu" width="50%" style="display=block; margin:auto"/>

The Edit menu contains actions for editing notebooks, including cut, copy, paste, and undo/redo. Here are some important shortcuts and functionalities:
- Like many text editors, <kbd>Ctrl</kbd>+<kbd>Z</kbd> and <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Z</kbd> are used to undo and redo actions inside a cell.
- Correspondingly, those shortcuts without <kbd>Ctrl</kbd> are used for cell operations. For example:
    - <kbd>Z</kbd> is used to undo the last cell operation.
    - <kbd>Shift</kbd>+<kbd>Z</kbd> is used to redo the last reverted cell operation.
    - <kbd>X</kbd>, <kbd>C</kbd>, and <kbd>V</kbd> are used to cut, copy, and paste cells.

<img src="Lesson 0/assets/menu_edit.png" alt="Edit menu" width="50%" style="display=block; margin:auto"/>

The Run menu contains actions for running and debugging notebooks, including running all cells, running a cell, and restarting the kernel. In most cases, you only need to remember that <kbd>Shift</kbd>+<kbd>Enter</kbd> is used to run a cell. If you want to render all Markdown cells or run all cells without restarting the kernel, you need to access it in this menu.

<img src="Lesson 0/assets/menu_run.png" alt="Run menu" width="50%" style="display=block; margin:auto"/>

The Kernel menu contains actions for managing kernels, including restarting, changing, and shutting down the kernel. For now, you can consider the kernel as the background process that runs your code and renders your Markdown cells. If you encounter any issues while running your code, you can try to restart the kernel, clear the output, and run the cell again. You can find the corresponding options in this menu.

<img src="Lesson 0/assets/menu_kernel.png" alt="Kernel menu" width="50%" style="display=block; margin:auto"/>

## About Jupyter Notebook

Some of you may hear about Jupyter Notebook, which is also a web-based interactive development environment. Before JupyterLab was released, Jupyter Notebook was the default interface for Jupyter. Now it is no longer recommended to use Jupyter Notebook, since the latest version of Jupyter Notebook is based on JupyterLab, which may eventually be merged into JupyterLab.

<img src="Lesson 0/assets/jupyter_notebook_interface.png" alt="Jupyter Notebook interface" width="50%" style="display=block; margin:auto"/>

## Other IDEs

There are many other IDEs for Python, such as [PyCharm](https://www.jetbrains.com/pycharm/), [Visual Studio Code](https://code.visualstudio.com/), and [Spyder](https://www.spyder-ide.org/). Each of them is designed for different purposes, and you can choose the one that best suits your needs.
