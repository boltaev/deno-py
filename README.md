# Deno
Deno is a Python console mini program for scraping data from a specific web page.

Deno collected from words "Data Entry Operator"

## Usage
First of all you need to specify name of file that you want to save
```python
filename = 'name_of_file.xls'
```

After that you can edit a url address. Then when you call a function for counting pages specify number of "first" and "last" pages. `[first, last)`

```python
products_links = count_items(3, 14)
```

## Results
After running the code, the process may go a little slower.
### 1. First stage program counts all pages then collects links to the items:
```
finish read page:  3
finish read page:  4
finish read page:  5
finish read page:  6
```

### 2. Second stage, visiting every items page and scrape data:

```
1 / 121  saving:  Портативный аккумулятор “J72 Easy travel” 10000mAh
2 / 121  saving:  Портативный аккумулятор “J42B High power” 30000mAh
3 / 121  saving:  Портативный аккумулятор “J62A Jove” 10000mAh с лампой

...

119 / 121  saving:  Power bank “J15 Contented” PD QC3.0 10000mAh
120 / 121  saving:  Power bank “J12 Amazing star” 10000 mAh
121 / 121  saving:  Power bank “J9 Camouflage series” 10000 mAh
```

### 3. Third stage, final message about successfully ending the process and some metrics:
```
extracted data saved successfully into:  HOCO_Powerbanks2.xls
elapsed time:  661.587
average elapsed time per item:  5.468
```
    
## Tutorial
I learned it from John Watson Rooney on YouTube tutorial video.

[Link to the video](https://youtu.be/nCuPv3tf2Hg)
