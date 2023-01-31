import srt, datetime, sys, os

argLen = len(sys.argv)
input = sys.argv[1]
inputFile = open(input, "r")
output = sys.argv[3]
outputFile = open(os.path.dirname(input)+"/"+output, "w")
data = inputFile.read()
subs = list(srt.parse(data))
subsLen = len(subs)
delay = float(sys.argv[2])

os.chdir(os.path.dirname(input))


if argLen != 4 :
    print("Error : Too much or missing arguments.")
elif input.endswith('.srt')== False :
    print("Wrong input file type. Need .srt file." )
elif input.endswith('.srt')== False :
    print("Wrong output file type. Name the generated file with .srt extension.")
else :
    for sub in range(0,subsLen) :
        subs[sub].start = subs[sub].start + datetime.timedelta(seconds = delay)
        subs[sub].end = subs[sub].end + datetime.timedelta(seconds = delay)

    outputFile.write(srt.compose(subs))
