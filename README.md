<p align="center">
  <img src="assets/banner.png" alt="Sorting Visualizer" width="100%"/>
</p>
This is a retro-style sorting algorithm visualizer that uses Streamlit for the interface and Plotly to generate the charts and graphs.
<p align="center">
</p>

## What it does

Generates a random array, then animates it being sorted with bubble sort, merge sort, quick sort, or selection sort, so you can actually see how each algorithm moves through the data. Alongside the animation, it shows live stats on comparisons and swaps, so the difference between an O(n²) algorithm and an O(n log n) one is visible, not just theoretical.

There's also an info page explaining how each algorithm works, with diagrams I made in Canva.
 <img src="assets/demo_image.png" alt="Demo image" width="100%"/>
## Run it locally

```bash
git clone https://github.com/FlXZ22/python-sorting-visualizer.git
cd python-sorting-visualizer
pip install -r requirements.txt
streamlit run main.py
```

## How it's built

I wrote each sorting algorithm as a function that takes an unsorted array and returns a list of snapshots, one per step, each one storing the array's state at that point plus which indices are being compared or swapped. `main.py` imports all of these and feeds the snapshots into Plotly to animate them.

For large arrays, recording every single step made the animation laggy, so I added a class in `utils.py` that only takes a snapshot every fixed interval instead, depending on which algorithm is running.

## File Breakdown

<img src="assets/file_structure.png" alt="file breakdown" width="100%"/>

- **main.py**: This is the core file of the program, and it starts by importing the functions from the files that contain the sorting algorithms. Then there is the title of the project, "Sorting Algorithms", followed by some input boxes for the number generator: minimum, maximum, and count. Next, there is a button that generates random unsorted numbers, which form the unsorted array that will be sorted and visualized by the program. I have implemented some validation checks: if the minimum is greater than the maximum, it displays an error message, and the same happens if the count is larger than the maximum.

  After that, there are four choices for how to sort the array: bubble sort, merge sort, quick sort, and selection sort, each with its own button. Clicking a button generates a graph along with a "Play" button, and clicking that starts the animation.

  I have also implemented a time calculator that shows how long the algorithm took to sort the array and how long the animation lasted. I then created an HTML table using divs that represents four values: comparisons, swaps, n squared, and n log. I copied this table's design from a CSS library.

  Lastly, there is a button that links to the info page, which explains how each algorithm works.

- **bubble_sort.py**: Contains the function `bubble_sort_steps`, an implementation of bubble sort that returns a list of snapshots which can later be animated.

- **merge_sort.py**: The same as bubble_sort.py, but using an implementation of merge sort instead. It returns a list of snapshots through a function called `merge_sort_steps`.

- **quick_sort.py**: Also the same as the rest, it contains a function called `quick_sort_steps`, an implementation of quick sort that returns a list of snapshots.

- **selection_sort.py**: Contains the function `selection_sort_steps`, an implementation of selection sort that returns a list of snapshots.

- **utils.py**: This file contains a class that creates a dictionary for each snapshot and improves performance when the count is very large by taking a snapshot only every few intervals, depending on the algorithm.

- **requirements.txt**: Contains the libraries essential to run the application.

- **img/**: Contains custom-made graphs to explain each algorithm, using images made by me with Canva.

- **pages/**: Contains `info.py`, a Streamlit page that explains how each algorithm works using images, and it is connected to main.py.

- **styles.css**: A CSS file that main.py and pages/info.py load using a function called `load_css`, which reads the file, stores it in a variable called `css`, and then injects it into the page with `st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)`.

- **.streamlit/**: A folder related to the design of the Streamlit web page, containing `config.toml`, which defines the background color, font, and other settings.

<img src="assets/full_demo_image.png" alt="Demo image" width="100%"/>

## Design Choices
I chose Streamlit simply because it was an easy pick for me; I had discovered it before Flask and other libraries.

I also gave the program a retro style, because in my opinion, it makes it look unique and different from other sorting algorithm visualizers.

In the first version of this program, I used a different library to generate static graph images instead of Plotly, but then I changed my mind because I wanted the graphs to be animated.

When I was creating the list of dictionaries, I used a simple class so the code was more organized and easier to understand, which also helped me learn how classes work in Python.

Another reason was that I implemented the comparisons and swaps table so the person using the visualizer could actually see what makes an algorithm quadratic versus logarithmic.

## AI use

No code here was AI-generated. I used Claude to debug and to get explanations for things I didn't understand yet, and Grammarly to clean up this README.

---

## Demo video

https://github.com/user-attachments/assets/cfd97cb9-4797-4f6d-8ec0-160b88038156

<p align="center">
  <b><a href="https://github.com/FlXZ22">Metis</a></b> · 16 · self-taught · Milan
</p>
