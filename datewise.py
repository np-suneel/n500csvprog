import glob
import os
import re
import time

folder_path = 'C:\\Users\\amdge\\Desktop\\ssd'
count = 1
print("Copying...")
for filename in glob.glob(os.path.join(folder_path, '*.csv')):

    with open(filename, "r") as f:  # open csv as f
        x = re.match(r"(C:\\Users\\amdge\\Desktop\\ssd)\\(.*).csv", filename)
        text = f.read()
        StockLines = text.split("\n")
        i = 1
        start = time.time()
        r = re.match("(\d{4}-\d{2}-\d{2}),(.*)", StockLines[i])
        olddt = r.group(1)
        with open("C:\\Users\\amdge\\Desktop\\DATEWISE\\" + r.group(1) + ".txt", "a+") as fj:  # open first date as fj
            if count == 1:
                fj.write("Time,Open,High,Low,Close,Volume,Stock\n")

            while StockLines[i] != "\0":

                # Counter += 1
                # print(CoList[i])
                r = re.match("(\d{4}-\d{2}-\d{2}),(.*)", StockLines[i])
                if r:
                    newdt = r.group(1)
                    if olddt != newdt:
                        olddt = r.group(1)
                        # fj.close()
                        fj = open("C:\\Users\\amdge\\Desktop\\DATEWISE\\" + olddt + ".txt", "a+")
                        if count == 1:
                            fj.write("Time,Open,High,Low,Close,Volume,Stock\n")
                        continue
                    fj.write(r.group(2) + "," + x.group(2) + "\n")
                    i += 1
                else:
                    # fj.close()
                    break
                # f.close()
        end = time.time()
        print(
            "Completed for " + x.group(2) + " stock" + ". Execution time: " + str(round((end - start), 2)) + " seconds")
    count = 2
print("Copied all files")
    