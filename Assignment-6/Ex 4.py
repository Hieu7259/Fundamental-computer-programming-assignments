text = "wo shi nei nei ge nei nei ge nei ge nei nei yang guang cai hong xao bai ma di di da di di da"
word_counts = {}
text = text.split()
for word in text :
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
sorted_list = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_list[:5]
sum_of_top_5 = sum(count for word, count in top_5)          
print("The 5 most frequent words are:", top_5)
proportion = sum_of_top_5 / len(text) * 100
print("The proportion of the 5 most frequent words is:", proportion,"%")