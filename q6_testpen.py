from Testing import testPenData, average, stDeviation
from time import time


def varyPtronsTestPenData():
    ptrons = 0
    testAccuracy = []
    while ptrons <= 40:
        nnet, ta = testPenData([ptrons])
        testAccuracy.append(ta)
        ptrons += 5
    return testAccuracy

if __name__ == '__main__':
    start = time()
    testAccuracy = varyPtronsTestPenData()
    # Calculate statistics
    maxTA = max(testAccuracy)
    meanTA = average(testAccuracy)
    stdevTA = stDeviation(testAccuracy)
    # Output to terminal
    print 'max:', maxTA
    print 'mean:', meanTA
    print 'stdev:', stdevTA
    # Output to file
    fout = open('NN Vary Hidden Perceptions on Test Pen Data.txt', 'w')
    fout.write('test accuracies: ' + str(testAccuracy) + '\n')
    fout.write('max: ' + str(maxTA) + '\n')
    fout.write('mean: ' + str(meanTA) + '\n')
    fout.write('stdev: ' + str(stdevTA) + '\n')
    end = time()
    executionTime = end - start
    fout.write('execution time: ' + str(executionTime) + ' seconds')
    print('execution time:', executionTime, 'seconds')
    fout.close()
