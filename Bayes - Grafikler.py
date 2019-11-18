import csv
import matplotlib.pyplot as plt
accuracy_values = []
t_list = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3500]
for t in t_list:
    print("*************************************\n"
          "\t\tÖrnek Tweet Sayısı:", t, "\n*************************************\n")
    tweets = []
    class_0 = []
    class_1 = []

    with open("train.csv", "r") as csv_file:
        csv_file.readline(1000)
        csv_reader = csv.reader(csv_file)
        next(csv_file)

        x = 0

        for line in csv_reader:
            if x < (0.8*t):
                x += 1
                if line[0] == "0":
                    class_0.append(line[2])
                else:
                    class_1.append(line[2])

    class_1_words = []
    for line in class_1:
        line = line.split(" ")
        line = list(filter(''.__ne__, line))
        for j in line[1:]:
            class_1_words.append(j)


    def erase_stop_words(liste):
        stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself"
                                                                                                           'yourselves',
                      "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself"
                                                                                                   "they", "them", "their",
                      "theirs", "themselves", "what", "which", "who", "whom", "this", "that"
                                                                                      "these", "those", "am", "is", "are",
                      "was", "were", "be", "been", "being", "have", "has", "had", "having"
                                                                                  "do", "does", "did", "doing", "a", "an",
                      "the", "and", "but", "if", "or", "because", "as", "until"
                                                                        "while", "of", "at", "by", "for", "with", "about",
                      "against", "between", "into", "through", "during"
                                                               "before", "after", "above", "below", "to", "from", "up",
                      "down", "in", "out", "on", "off", "over", "under"
                                                                "again", "further", "then", "once", "here", "there", "when",
                      "where", "why", "how", "all", "any"
                                                    "both", "each", "few", "more", "most", "other", "some", "such", "no",
                      "nor", "not", "only", "own"
                                            "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don",
                      "should"
                      "now"]  # internet üzerinden en çok kullanılan stop words değerleri bulundu
        x = 0
        while x < 9:
            x += 1
            for t in liste:
                for p in stop_words:
                    if t == p:
                        liste.remove(t)


    class_1_words2 = []

    for i in class_1_words:
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
        class_1_words2.append(i)

    class_1_words3 = []
    for i in class_1_words2:
        if "*" in i:
            pass
        else:
            class_1_words3.append(i)

    class_1_words4 = []
    for i in range(len(class_1_words3)):
        i = class_1_words3[i].lower()
        class_1_words4.append(i)
    print("*Class 1'de bulunan tweet sayısı:", len(class_1))
    print("*Class 1'de bununan kelime sayısı:", len(class_1_words4), "\n")
    erase_stop_words(class_1_words4)
    print("*Class 1'de ayıklanmış kelime sayısı:", len(class_1_words4), "\n")


    class_0_words = []
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


    vocabulary = class_0_words4 + class_1_words4
    print("Vocabulary'de bulunan kelime sayısı (n):", len(vocabulary), "\n")

    print("Words in neutral tweets:", class_0_words4)
    print("Words in insulting tweets:", class_1_words4)

    #####################################################

    with open("test_with_solutions.csv", "r") as csv_test:
        csv_test.readline(1000)
        csv_test_reader = csv.reader(csv_test)

        test_class_0 = []
        test_class_1 = []
        test_samples = []

        x = 0
        for line in csv_test_reader:
            if x < (0.2*t):
                x += 1
                if line[0] == "0":
                    test_class_0.append(line[2])
                    test_samples.append(line[2])
                else:
                    test_class_1.append(line[2])
                    test_samples.append(line[2])

    true_test_values = []
    k = 0
    for i in test_samples:
        k += 1
        if i in test_class_0:
            true_test_values.append(0)
        else:
            true_test_values.append(1)

    test_values = []
    sample_tweets = []
    for line in test_samples:
        line = line.split(" ")
        line = list(filter(''.__ne__, line))
        sample_tweets.append(line)

    sayi = 0
    for k in sample_tweets:
        sayi += 1

        correct_tweets1 = []

        for i in k:
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

        for i in correct_tweets1:
            if "*" in i:
                pass
            else:
                correct_tweets2.append(i)

        correct_tweets3 = []
        for i in range(len(correct_tweets2)):
            i = correct_tweets2[i].lower()
            correct_tweets3.append(i)

        sample_words = []
        for i in correct_tweets3:
            if i in vocabulary:
                sample_words.append(i)
            else:
                pass

        bayes_i0 = []
        for i in sample_words:
            i0 = 1

            for j in class_0_words4:

                if i == j:
                    i0 += 1

            bayes_i0.append(i0 / (len(class_0_words4) + len(vocabulary)))

        j = -1
        for i in sample_words:
            j += 1

        bayes_i1 = []
        for i in sample_words:
            i1 = 1

            for j in class_1_words4:

                if i == j:
                    i1 += 1

            bayes_i1.append(i1 / (len(class_1_words4) + len(vocabulary)))

        h_non_spam = 0.5
        for i in bayes_i0:
            h_non_spam *= i

        h_spam = 0.5
        for i in bayes_i1:
            h_spam *= i

        if h_spam > h_non_spam:
            test_values.append(1)
        else:
            test_values.append(0)

    print("\n", "1: Insulting tweets", "0: Neutral tweets")
    print("Actual classes of test tweets: \t\t", true_test_values)
    print("Predicted classes of test tweets: \t", test_values)

    accuracy = 0
    for i in range(0, int(0.2*t)):
        if test_values[i] == true_test_values[i]:
            accuracy += 1

    accuracy_percent = (accuracy/(0.2*t))
    print("Doğru tahmin edilen tweet sayısı: ", accuracy)
    print("Accuracy = %", accuracy_percent*100)
    accuracy_values.append(accuracy_percent*100)

plt.plot(t_list, accuracy_values)
plt.ylabel("Accuracy (%)")
plt.xlabel("Sample Data Size")
plt.title("Relationship Between Accuracy and Sample Data Size")
plt.grid()
plt.show()
