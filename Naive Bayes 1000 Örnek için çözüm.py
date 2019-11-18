import csv  # veriyi içeri aktarmak için kullanıldı

tweets = []
class_0 = []
class_1 = []

with open("train.csv", "r") as csv_file:    # train.csv dosyası okundu
    csv_file.readline(1000)
    csv_reader = csv.reader(csv_file)
    next(csv_file)

    x = 0                                   # x değişkeni ile tweet sayısı kontrol edildi

    for line in csv_reader:
        if x < 800:                         # ilk aşamada toplamda 800 tweet kullanıldı
            x += 1
            if line[0] == "0":              # tweetlerin sınıfları belirlendi ve daha sonra kullanılmak için ayrıldı
                class_0.append(line[2])     # neutral tweetlerlerin comment değeleri ayrı listeye kondu
            else:
                class_1.append(line[2])     # insulting tweetlerlerin comment değeleri ayrı listeye kondu

class_1_words = []
for line in class_1:                        # insult içeren tweetlerdeki kelimeler ayrıldı ve boşluklar temizlendi
    line = line.split(" ")
    line = list(filter(''.__ne__, line))
    for j in line[1:]:
        class_1_words.append(j)             # temizlenen kelimeler ayrı bir listeye alındı


def erase_stop_words(liste):  # en çok kullanılan stop word için bir temizleme fonksiyonu yazıldı
    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                  'yourselves', "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", 'itself',
                  'they', "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
                  "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
                  "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as",
                  "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through",
                  "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off",
                  "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how",
                  "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not",
                  "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should"
                  "now"]
    l = 0
    while l < 9:            # while döngüsü ile örnek tweet içerisindeki her bir kelime ile eşleşen stop words,
        l += 1              # silindi ve 9 kere bu döngü tekrar ettirildi
        for t in liste:
            for p in stop_words:
                if t == p:
                    liste.remove(t)


class_1_words2 = []

for i in class_1_words:     # elde kalan kelimeler içerisinden anlam ifade etmeyen semboller temizlendi
    i = i.replace(".", "")
    i = i.replace(",", "")
    i = i.replace("?", "")
    i = i.replace("!", "")
    i = i.replace("@", "*")
    i = i.replace("&", "*")
    i = i.replace("(", "")
    i = i.replace(")", "")
    i = i.replace("-", "*")
    i = i.replace('"', "")
    i = i.replace("/", "")
    i = i.replace("\\", "*")
    i = i.replace("%", "*")
    i = i.replace("=", "*")
    i = i.replace("[", "")
    i = i.replace("]", "")
    i = i.replace(";", "")
    i = i.replace("_", "")
    i = i.replace("http", "*")  #bu tarz içerikler "*" sembolü ile değiştirildi
    i = i.replace("<", "*")
    i = i.replace(">", "*")
    class_1_words2.append(i)

class_1_words3 = []
for i in class_1_words2:        # "*" sembolü içeren kelimeler silinerek daha temiz ve anlamlı kelimeler elde edildi
    if "*" in i:
        pass
    else:
        class_1_words3.append(i)

class_1_words4 = []
for i in range(len(class_1_words3)):    #büyük küçük harf farklılığının önüne geçmek için tüm harfler küçültüldü
    i = class_1_words3[i].lower()
    class_1_words4.append(i)

print("*Class 1'de bulunan tweet sayısı:", len(class_1))                      # toplam tweet sayısı belirlendi
print("*Class 1'de bununan kelime sayısı:", len(class_1_words4), "\n")        # toplam kelime sayısı belirlendi
erase_stop_words(class_1_words4)                                              # stop words silindi
print("*Class 1'de ayıklanmış kelime sayısı:", len(class_1_words4), "\n")     # kalan kelime sayısı belirlendi

class_0_words = []              # Tüm bu işlemler insult içermeyen tweetler için yeniden yapıldı
for line in class_0:
    line = line.split(" ")
    line = list(filter(''.__ne__, line))
    for j in line[1:]:
        class_0_words.append(j)

class_0_words2 = []

for i in class_0_words:
    i = i.replace("ing", "")
    i = i.replace(".", "")
    i = i.replace(",", "")
    i = i.replace("?", "")
    i = i.replace("!", "")
    i = i.replace("@", "*")
    i = i.replace("&", "*")
    i = i.replace("(", "")
    i = i.replace(")", "")
    i = i.replace("-", "*")
    i = i.replace('"', "")
    i = i.replace("/", "")
    i = i.replace("\\", "*")
    i = i.replace("%", "*")
    i = i.replace("=", "*")
    i = i.replace("[", "")
    i = i.replace("]", "")
    i = i.replace(";", "")
    i = i.replace("_", " ")
    i = i.replace("http", "*")
    i = i.replace("<", "*")
    i = i.replace(">", "*")
    class_0_words2.append(i)

class_0_words3 = []
for i in class_0_words2:
    if "*" in i:
        pass
    else:
        class_0_words3.append(i)

class_0_words4 = []
for i in range(len(class_0_words3)):
    i = class_0_words3[i].lower()
    class_0_words4.append(i)

print("*Class 0 tweet sayısı:", len(class_0))
print("*Class 0 kelime sayısı:", len(class_0_words4), "\n")
erase_stop_words(class_0_words4)
print("*Class 0 ayıklanmış kelime sayısı:", len(class_0_words4), "\n")

vocabulary = class_0_words4 + class_1_words4            # iki ayrı sınıfta temizlenen kelimeler vocabulary'e eklendi

print("\n", "Vocabulary'de bulunan kelime sayısı (n):", len(vocabulary))

print("Words in neutral tweets:", class_0_words4)       # Normal tweetlerdeki kelimeler belirlendi
print("Words in insulting tweets:", class_1_words4)     # Hakaret içeren tweetlerdeki kelimeler belirlendi

#########################   2. Aşama    ############################

with open("test_with_solutions.csv", "r") as csv_test:      # test edilecek tweet örnekleri eklendi
    csv_test.readline(1000)
    csv_test_reader = csv.reader(csv_test)

    test_class_0 = []
    test_class_1 = []
    test_samples = []

    x = 0
    for line in csv_test_reader:
        if x < 200:                      # x değişkeni ile test tweetlerinin sayısı kontrol edildi
            x += 1
            if line[0] == "0":
                test_class_0.append(line[2])    # neutral tweetlerlerin comment değeleri ayrı listeye kondu
                test_samples.append(line[2])    # test edilecek tweet örnekleri listeye eklendi
            else:
                test_class_1.append(line[2])    # insulting tweetlerlerin comment değeleri ayrı listeye kondu
                test_samples.append(line[2])

true_test_values = []                           # accuracy hesabı için tweetlerin gerçek classları belirlendi
k = 0
for i in test_samples:
    k += 1
    if i in test_class_0:
        print(k, ". tweet: ", "Class: 0", i)
        true_test_values.append(0)              # bu değerler bir listeye "1" ve "0" olarak eklendi
    else:
        print(k, ". tweet: ", "Class: 1", i)
        true_test_values.append(1)

test_values = []
sample_tweets = []
for line in test_samples:
    line = line.split(" ")                      # gelen örnek kelimelere ayrıldı
    line = list(filter(''.__ne__, line))        # boşluklar silindi
    sample_tweets.append(line)

sayi = 0
for k in sample_tweets:
    sayi += 1

    correct_tweets1 = []

    for i in k:                                 # her bir örnekteki kelimeler temizlendi
        i = i.replace("ing", "")
        i = i.replace(".", "")
        i = i.replace(",", "")
        i = i.replace("?", "")
        i = i.replace("!", "")
        i = i.replace("@", "*")
        i = i.replace("&", "*")
        i = i.replace("(", "")
        i = i.replace(")", "")
        i = i.replace("-", "*")
        i = i.replace('"', "")
        i = i.replace("/", "")
        i = i.replace("\\", "*")
        i = i.replace("%", "*")
        i = i.replace("=", "*")
        i = i.replace("[", "")
        i = i.replace("]", "")
        i = i.replace(";", "")
        i = i.replace("_", "")
        i = i.replace("http", "*")
        i = i.replace("<", "*")
        i = i.replace(">", "*")
        correct_tweets1.append(i)

    correct_tweets2 = []

    for i in correct_tweets1:                   #  "*" lanan kelimeler silindi
        if "*" in i:
            pass
        else:
            correct_tweets2.append(i)

    correct_tweets3 = []                        # tüm kelimeler küçük harfle yazıldı
    for i in range(len(correct_tweets2)):
        i = correct_tweets2[i].lower()
        correct_tweets3.append(i)
    print("\n", sayi, ".Tweet içerisinde bulunan kelimeler: ", correct_tweets3)

    sample_words = []
    for i in correct_tweets3:                   # elde edilen tweetlerin içinde bulunan ve vocabulary ile eşleşen,
        if i in vocabulary:                     # kelimeler ayrı bir listeye değerlendirilmek üzere alındı,
            sample_words.append(i)
        else:
            pass

    bayes_i0 = []
    for i in sample_words:              # ayrılan bu kelimeler eğer neutral yorumlar ile eşleşiyorsa ihtimal hesaplandı
        i0 = 1                          # 1 den başlama sebebi hiç olmama ihtimaline göre "m-estimate" işlemi yapmak

        for j in class_0_words4:

            if i == j:
                i0 += 1

        bayes_i0.append(i0 / (len(class_0_words4) + len(vocabulary)))   # eşleşenlerin olasılığı hesaplandı

    j = -1
    for i in sample_words:              # aynı işlemler insulting yorumlar içinde yapıldı
        j += 1

    bayes_i1 = []
    for i in sample_words:
        i1 = 1

        for j in class_1_words4:

            if i == j:
                i1 += 1

        bayes_i1.append(i1 / (len(class_1_words4) + len(vocabulary)))

    h_non_spam = 0.5                         # sınıf ihtimali 1/2
    for i in bayes_i0:                       # bayes' teoreminde bahsedildiği üzere ile tüm olasılıklar çarpıldı
        h_non_spam *= i                      # spam olmama ihtimali hesaplandı
    print("Neutral olma ihtimali:", h_non_spam)

    h_spam = 0.5
    for i in bayes_i1:
        h_spam *= i                         # spam olma ihtimali hesaplandı
    print("Insult olma ihtimali:", h_spam)

    if h_spam > h_non_spam:                 # hesaplanan ihtimallere göre bir sınıflandırma yapıldı
        print("****Insult****")               # karşılaştırılmak üzere 1 ve 0 değerleri üzerinden liste oluşturuldu
        test_values.append(1)
    else:
        print("****Neutral****")
        test_values.append(0)

print("\n", "1: Insulting tweets", "0: Neutral tweets")
print("Actual classes of test tweets: \t\t", true_test_values)      # gerçek sınıf değerleri
print("Predicted classes of test tweets: \t", test_values)          # tahmin edilen sınıf değerleri

accuracy = 0
for i in range(0, 200):                     #accuracy hesabı için tahmin edilen her bir değer için 1 artırıldı
    if test_values[i] == true_test_values[i]:
        accuracy += 1

tp = 0
fn = 0
tn = 0
fp = 0
for i in range(0, 200):
    if test_values[i] == 0 and true_test_values[i] == 0:        # test sonuçlarının tahminlerine göre,
        tp += 1
    elif test_values[i] == 1 and true_test_values[i] == 0:      # confusion matrix için değerler bulundu
        fp += 1
    elif test_values[i] == 0 and true_test_values[i] == 1:
        fn += 1
    elif test_values[i] == 1 and true_test_values[i] == 1:
        tn += 1

accuracy_percent = (accuracy / 200)*100         # elde edilen değer sample sayısına bölünerek yüzde bulundu
print("Doğru tahmin edilen tweet sayısı: ", accuracy)
print("Accuracy = %", accuracy_percent)

print("\n\t\t---Confusion Matrix---\t\t\n"      # confusion matrix oluşturuldu
      "\tPredicted: \tNeutral\t\tInsult",
      "\nAcutal: ",
      "\nNeutral\t\t\t", tp, "\t\t", fn,
      "\nInsult\t\t\t", fp, "\t\t\t", tn)

print("\nTrue Positive:", tp, "/ False Negative:", fn, "/ False Positive:", fp, "/ True Negative:", tn, )
precision = (tp / (tp + fp))                    # precision ve recall hesaplandı
recall = (tp / (tp + fn))
f1_score = (2 * recall * precision) / (recall + precision)          # f - measure hesaplandı
print("Precision: \t", precision, "\nRecall:\t\t", recall, "\nF-1 Score: \t", f1_score)
