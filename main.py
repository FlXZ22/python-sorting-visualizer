import time
import random

import streamlit as st
import plotly.graph_objects as go

from merge_sort import merge_sort_steps
from bubble_sort import bubble_sort_steps
from quick_sort import quick_sort_steps
from selection_sort import selection_sort_steps

if "n" not in st.session_state:
    st.session_state.n = []
if "algo" not in st.session_state:
    st.session_state.algo = None

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
.title {
    background: #2e2e2e;
    font-family: "Press Start 2P", system-ui !important;
    font-size: 24px !important;
    box-shadow: 0px 5px black, 0px -5px black, 5px 0px black, -5px 0px black, 0px 10px #00000038, 5px 5px #00000038, -5px 5px #00000038, inset 0px 5px #ffffff1f, inset 0px -5px #00000030;
}

.st-key-bubble button {
    background-color: #6abc3a !important;
    color: #fff !important;
    padding: 15px 40px !important;
    margin: 10px !important;
    font-size: 14px !important;
    font-family: 'Press Start 2P', system-ui !important;
    border: 0 !important;
    border-radius: 0 !important;
    box-shadow:
        0px 5px black,
        0px -5px black,
        5px 0px black,
        -5px 0px black,
        0px 10px #00000038,
        5px 5px #00000038,
        -5px 5px #00000038,
        inset 0px 5px #ffffff36 !important;
    cursor: pointer !important;
}

.st-key-bubble button:active {
    transform: translateY(5px);
    box-shadow:
        0px 5px black,
        0px -5px black,
        5px 0px black,
        -5px 0px black,
        inset 0px 5px #00000038 !important;
}

.st-key-merge button {
    background-color: #d83433 !important;
    color: #fff !important;
    padding: 15px 40px !important;
    margin: 10px !important;
    font-size: 14px !important;
    font-family: 'Press Start 2P', system-ui !important;
    border: 0 !important;
    border-radius: 0 !important;
    box-shadow:
        0px 5px black,
        0px -5px black,
        5px 0px black,
        -5px 0px black,
        0px 10px #00000038,
        5px 5px #00000038,
        -5px 5px #00000038,
        inset 0px 5px #ffffff36 !important;
    cursor: pointer !important;
}

.st-key-merge button:active {
    transform: translateY(5px);
    box-shadow:
        0px 5px black,
        0px -5px black,
        5px 0px black,
        -5px 0px black,
        inset 0px 5px #00000038 !important;
}
.st-key-generate button {
    background-color: #38667f !important;
    color: #fff !important;
    padding: 15px 40px !important;
    margin: 10px !important;
    font-size: 14px !important;
    font-family: 'Press Start 2P', system-ui !important;
    border: 0 !important;
    border-radius: 0 !important;
    box-shadow:
        0px 5px black,
        0px -5px black,
        5px 0px black,
        -5px 0px black,
        0px 10px #00000038, 
        5px 5px #00000038,
        -5px 5px #00000038,
        inset 0px 5px #ffffff36 !important;
    cursor: pointer !important;
}

.st-key-generate button:active {
    transform: translateY(5px);
    box-shadow:
        0px 5px black,
        0px -5px black,
        5px 0px black,
        -5px 0px black,
        inset 0px 5px #00000038 !important;
}
.st-key-quick button {
    background-color: #9f7db1 !important;
    color: #fff !important;
    padding: 15px 40px !important;
    margin: 10px !important;
    font-size: 14px !important;
    font-family: 'Press Start 2P', system-ui !important;
    border: 0 !important;
    border-radius: 0 !important;
    box-shadow:
        0px 5px black,
        0px -5px black,
        5px 0px black,
        -5px 0px black,
        0px 10px #00000038, 
        5px 5px #00000038,
        -5px 5px #00000038,
        inset 0px 5px #ffffff36 !important;
    cursor: pointer !important;
}
.st-key-quick button:active {
    transform: translateY(5px);
    box-shadow:
        0px 5px black,
        0px -5px black,
        5px 0px black,
        -5px 0px black,
        inset 0px 5px #00000038 !important;
}

.st-key-selection button {
    background-color: #009688 !important;
    color: #fff !important;
    padding: 15px 40px !important;
    margin: 10px !important;
    font-size: 14px !important;
    font-family: 'Press Start 2P', system-ui !important;
    border: 0 !important;
    border-radius: 0 !important;
    box-shadow:
        0px 5px black,
        0px -5px black,
        5px 0px black,
        -5px 0px black,
        0px 10px #00000038, 
        5px 5px #00000038,
        -5px 5px #00000038,
        inset 0px 5px #ffffff36 !important;
    cursor: pointer !important;
}
.st-key-selection button:active {
    transform: translateY(5px);
    box-shadow:
        0px 5px black,
        0px -5px black,
        5px 0px black,
        -5px 0px black,
        inset 0px 5px #00000038 !important;
}

p, h1, h2, h3, label, button, input {
    font-family: 'Press Start 2P', system-ui !important;
}

</style>
""",
    unsafe_allow_html=True,
)

# Title
st.markdown(
    "<h1 class='title' style='color: white; padding: 15px; margin-bottom: 30px;'>Sorting Algorithms</h1>",
    unsafe_allow_html=True,
)

# Minimum and maximum and count inputs
minimum = st.number_input("Minimum", min_value=0, value=1, step=1)
maximum = st.number_input("Maximum", min_value=1, value=100, step=1)
count = st.number_input("Count", min_value=1, max_value=10000, value=50, step=1)


def handle_generate_numbers(minimum, maximum, count):
    generate_number = st.button(
        "Generate Random Numbers", use_container_width=True, key="generate"
    )
    if generate_number:
        st.session_state.algo = None
        if maximum <= minimum:
            st.error("Maximum must be greater than minimum.")
            st.session_state.n = []
        elif count > 10000:
            st.error("Count must be less than 10000")
            st.session_state.n = []
        else:
            range_size = maximum - minimum + 1
            if count > range_size:
                st.warning(
                    "Count is larger than the selected range; using the full range instead."
                )
                st.session_state.n = random.sample(
                    range(minimum, maximum + 1), range_size
                )
            else:
                st.session_state.n = random.sample(range(minimum, maximum + 1), count)
        


handle_generate_numbers(minimum, maximum, count)


def show_numbers():

    st.markdown(
        "<p style='display: flex; justify-content: center;'>Random Numbers</p>",
        unsafe_allow_html=True,
    )

    visible_numbers = st.session_state.n[:10]
    box = ""
    for number in visible_numbers:
        box += f"<div align='center' style='background-color: white; color: black; padding: 2px; border: 2px solid #5a3d00; width: 40px; height: 40px; font-weight: bold; border-radius: 2px; box-shadow: 2px 2px 0px 0px #5a3d00;'>{number}</div>"
    html = f"<div style='display:flex; justify-content: center; gap: 4px; '>{box}</div>"
    st.markdown(f"{html}", unsafe_allow_html=True)
    if len(st.session_state.n) > 10:
        st.markdown(
            "<p style='display: flex; justify-content: center;'>...</p>",
            unsafe_allow_html=True,
        )


show_numbers()


speed = st.slider("Speed: ", 1, 50, 5)


def render_frames(steps, key, title, n, speed):
    def colors_for_step(step, default_color="#009688", highlight_color="#d83433"):
        # apply the highlights color to the highlights indices and apply the default color to the rest in range(len(step["array"]))
        colors = [
            highlight_color if i in step["highlight_indices"] else default_color
            for i in range(len(step["array"]))
        ]
        return colors

    if not steps:
        st.warning("There is no step to show")
        return
    if len(n) < 5:
        st.warning("n must be greter than 5")
        return
    placeholder = st.empty()
    frames = []
    for i, step in enumerate(steps):
        frames.append(
            go.Frame(
                data=[
                    go.Bar(
                        x=list(range(len(step["array"]))),
                        y=step["array"],
                        marker_color=colors_for_step(step),
                    )
                ],
                name=str(i),
            )
        )
    fig = go.Figure(
        data=[
            go.Bar(
                x=list(range(len(steps[0]["array"]))),
                y=steps[0]["array"],
                marker_color=colors_for_step(steps[0]),
            )
        ],
        frames=frames,
    )
    fig.update_layout(
        title_text=f"{title}",
        yaxis_range=[0, max(n) + 1],
        updatemenus=[
            dict(
                type="buttons",
                direction="up",
                showactive=False,
                x=0.0,
                y=-0.2,
                xanchor="left",
                yanchor="top",
                bgcolor="#F4EFE1",
                bordercolor="#333333",
                borderwidth=1,
                pad={"r": 16, "t": 16, "l": 16, "b": 16},
                font=dict(family="Press Start 2P, system-ui", size=11, color="black"),
                buttons=[
                    dict(
                        label="Play",
                        method="animate",
                        args=[
                            None,
                            {
                                "frame": {"duration": 1000 // speed, "redraw" : True},
                                "transition": {"duration": 0},
                                "fromcurrent": True,
                            },
                        ],
                    )
                ],
            )
        ],
    )
    with placeholder.container():
        st.plotly_chart(fig, use_container_width=True, key=f"{key}")


def run_algorithm(name, sort_function, speed, n, key):

    st.write(f"{name} sort started...")
    start_time = time.perf_counter()
    steps = sort_function(n.copy())
    end_time = time.perf_counter()
    st.success(
        f"The {name} sort algorithm finished in {end_time - start_time:.6f} seconds"
    )

    render_frames(steps, f"{key}_{hash(tuple(n))}", f"{name} Sort", n, speed)

    animation_time = len(steps) * (1000 // speed) / 1000
    st.info(f"The animation finished in {animation_time:.6f} seconds")


def draw_sort(n):
    # Create col
    # ums for the buttons
    (
        col1,
        col2,
    ) = st.columns(2)
    with col1:
        bubble_clicked = st.button(
            "Bubble Sort", use_container_width=True, key="bubble"
        )

    with col2:
        merge_clicked = st.button("Merge Sort", use_container_width=True, key="merge")

    col3, col4 = st.columns(2)

    with col3:
        quick_clicked = st.button("Quick Sort", use_container_width=True, key="quick")
    with col4:
        selection_clicked = st.button(
            "Selection Sort", use_container_width=True, key="selection"
        )

    if merge_clicked:
        st.session_state.algo = "merge"
    if bubble_clicked:
        st.session_state.algo = "bubble"
    if quick_clicked:
        st.session_state.algo = "quick"
    if selection_clicked:
        st.session_state.algo = "selection"

    if not n:
        st.session_state.algo = None
        st.error(
            "The variable n is empty, please generate random numbers to start the visualization"
        )
    else:

        # merge sort
        if st.session_state.algo == "merge":
            run_algorithm("Merge", merge_sort_steps, speed, n, "merge_key")

        # bubble sort
        elif st.session_state.algo == "bubble":
            run_algorithm("Bubble", bubble_sort_steps, speed, n, "bubble_key")

        # Quick sort
        elif st.session_state.algo == "quick":
            run_algorithm("Quick", quick_sort_steps, speed, n, "quick_key")

        elif st.session_state.algo == "selection":
            run_algorithm("Selection", selection_sort_steps, speed, n, "selection_key")


draw_sort(st.session_state.n)
