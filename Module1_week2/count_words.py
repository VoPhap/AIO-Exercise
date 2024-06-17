
def word_count(file):
    word_count = {} 
    with open(file, 'r') as f:
            lines = f.readlines()

    for line in lines:   
        line = line.lower()
        line = line.replace('.', '').replace(',' , '')
        words = line.split()
        
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1 
    

    return word_count

file_path = 'C:/Users/Dell/Desktop/AIO-Exercise/AIO-Exercise/Module1_week2/P1_data.txt'
print(word_count (file_path))