import streamlit as st

def load_css(path: str) ->None:
    with open(path) as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

load_css("styles.css")

tab1, tab2, tab3, tab4 = st.tabs(['Bubble', 'Merge', 'Selection', 'Quick'])

with tab1:
    st.markdown(
        "<h1 class='title-info' style='color: white; padding: 15px; margin-bottom: 30px;'>Bubble Sort</h1>",
        unsafe_allow_html=True,
    )
    st.markdown('''<p style='font-size:small;'>
    <strong>Bubble sort</strong> is the simplest sorting method out there. It walks through the array over and over, comparing neighboring pairs and swapping them when they're in the wrong order. Enough passes like that and the whole array ends up sorted.
    </p>''', unsafe_allow_html=True)
    st.image("img/Bubble_sort_2.png")
    st.image("img/Bubble_sort_3.png")
    st.markdown('''
    <p>How it works, step by step</p>
    <ul style='font-size:small;'>
        <li>Compare each pair of neighboring elements, swap them if the left one is bigger than the right one.</li>
        <li>After one full pass, the largest remaining value has bubbled to the end of the array.</li>
        <li>Repeat the pass on what's left, ignoring the elements already placed at the end.</li>
        <li>If a full pass goes by with no swaps, the array is already sorted, so it stops early.</li>
    </ul>
    <p><strong>Complexity</strong></p>
    <ul style='font-size:small;'>
        <li><strong>Time</strong>: O(n&sup2;) on average and in the worst case. With the early stop check, an already sorted array only takes O(n).</li>
        <li><strong>Space</strong>: O(1), it sorts in place and only needs room to hold one value during a swap.</li>
    </ul>
    ''', unsafe_allow_html=True)
with tab2:
    st.markdown(
        "<h1 class='title-info' style='color: white; padding: 15px; margin-bottom: 30px;'>Merge Sort</h1>",
        unsafe_allow_html=True,
    )
    st.markdown('''<p style='font-size:small;'>
    <strong>Merge sort</strong> is an efficient, stable sorting algorithm that uses a divide-and-conquer approach. It splits the array into two halves, sorts each half recursively, then merges them back together.
    </p>
    ''', unsafe_allow_html=True)
    st.image("img/merge_sort.png")
    st.markdown('''
    <p>How it works, step by step</p>
    <ul style='font-size:small;'>
        <li><strong>Divide</strong>: Split the array into two halves, again and again, until each piece has only one element.</li>
        <li><strong>Conquer</strong>: A single-element piece is already sorted, so there's nothing to do here.</li>
        <li><strong>Merge</strong>: Combine the sorted pieces back together in order, until one full sorted array is left.</li>
    </ul>
    ''', unsafe_allow_html=True)
    st.markdown('''
    <p>Here's the example above, worked through:</p>
    <p style='font-size:small;'><strong>Divide:</strong></p>
    <ul style='font-size:small;'>
        <li>[38, 27, 43, 10] splits into [38, 27] and [43, 10].</li>
        <li>[38, 27] splits into [38] and [27].</li>
        <li>[43, 10] splits into [43] and [10].</li>
    </ul>
    <p style='font-size:small;'><strong>Conquer:</strong> each single element ([38], [27], [43], [10]) is already sorted on its own.</p>
    <p style='font-size:small;'><strong>Merge:</strong></p>
    <ul style='font-size:small;'>
        <li>[38] and [27] merge into [27, 38].</li>
        <li>[43] and [10] merge into [10, 43].</li>
        <li>[27, 38] and [10, 43] merge into [10, 27, 38, 43].</li>
    </ul>
    <p style='font-size:small;'>Final sorted array: [10, 27, 38, 43].</p>
    <p><strong>Complexity</strong></p>
    <ul style='font-size:small;'>
        <li><strong>Time</strong>: O(n log n) in every case, best, average, and worst.</li>
        <li><strong>Space</strong>: O(n), because merging needs a temporary array to hold elements while combining.</li>
    </ul>
    ''', unsafe_allow_html=True)


with tab3:
    st.markdown(
        "<h1 class='title-info' style='color: white; padding: 15px; margin-bottom: 30px;'>Selection Sort</h1>",
        unsafe_allow_html=True,
    )
    st.markdown('''<p style='font-size:small;'>
    <strong>Selection sort</strong> splits the array into a sorted part and an unsorted part. Each round it hunts down the smallest value left in the unsorted part and swaps it into place at the front of that section.
    </p>''', unsafe_allow_html=True)
    
    st.image("img/selection_sort.png")
    st.markdown('''
    <p>How it works, step by step</p>
    <ul style='font-size:small;'>
        <li>Scan the unsorted portion of the array and find its smallest element.</li>
        <li>Swap that element with the first slot of the unsorted portion.</li>
        <li>Move the boundary between sorted and unsorted one slot to the right.</li>
        <li>Keep repeating until the unsorted portion shrinks to nothing.</li>
    </ul>
    <p><strong>Complexity</strong></p>
    <ul style='font-size:small;'>
        <li><strong>Time</strong>: O(n&sup2;) in every case, best, average, and worst, since it always scans the remaining elements for the minimum no matter how sorted things already are.</li>
        <li><strong>Space</strong>: O(1), only a couple of variables are needed to do the swap.</li>
    </ul>
    ''', unsafe_allow_html=True)
with tab4:
    st.markdown(
        "<h1 class='title-info' style='color: white; padding: 15px; margin-bottom: 30px;'>Quick Sort</h1>",
        unsafe_allow_html=True,
    )
    st.markdown('''<p style='font-size:small;'>
    <strong>Quick sort</strong> picks one element as a pivot, then rearranges the array so everything smaller lands on the pivot's left and everything bigger lands on its right. Run that same trick recursively on each side and the whole array ends up sorted.
    </p>''', unsafe_allow_html=True)
    st.image("img/quick_sort.png")
    st.markdown('''
    <p>How it works, step by step</p>
    <ul style='font-size:small;'>
        <li>Pick a pivot, could be the first element, the last one, a random pick, or the median.</li>
        <li>Partition the array around it: push smaller elements to the pivot's left, bigger ones to its right.</li>
        <li>Recursively run the same steps on the left chunk and the right chunk.</li>
        <li>Stop recursing once a chunk is down to one element or empty, it's already sorted at that point.</li>
    </ul>
    <p><strong>Complexity</strong></p>
    <ul style='font-size:small;'>
        <li><strong>Time</strong>: best and average case land at O(n log n), when the pivot roughly splits the array in half each round. Worst case drops to O(n&sup2;), which happens when the pivot keeps landing on the smallest or largest value, like sorting an already sorted array with a bad pivot choice.</li>
        <li><strong>Space</strong>: O(log n) in the best case with a balanced recursion tree, up to O(n) in the worst case when the partitions are lopsided.</li>
    </ul>
    ''', unsafe_allow_html=True)

