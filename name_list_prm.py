import regex

with open('writer_name_no_repeat.txt') as file:
    lst = file.readlines()
pre_finder = regex.compile(r'^([\p{Han}\p{Katakana}\p{Hiragana}]+) ([\p{Han}|\p{Katakana}\p{Hiragana}\p{Common}]+)\n')
pre2_finder = regex.compile(r'^((\p{Han}|\p{Katakana}|\p{Hiragana})+) \n$')
x=0
assaa=0
with open('auto_complete_list.txt', 'w')as file:
    for line in lst:
        # print(line)
        pre = pre_finder.match(line)
        pre2 = pre2_finder.match(line)
        if pre!=None :
            print(pre.group(2))
            pre=pre.group(1)+'　'+pre.group(2)
           # pre=str(pre)
            print(pre.split(),'1')
            a1=len(pre.split()[0])
            #a1=a1.append('space')
            print(a1)
            a2=len(pre.split()[1])
            print(a2)
            pre=a1+a2
            b = 1
            prelst=list(range(a1))
            prelst.append('space')
            print(prelst)
            prelst=prelst+list(range(a1,a1+a2))
            for i in prelst:
              if i != 'space' :
                if b >= 0:
                  if b>=a1:
                      a = line[0:a1]+line[a1+1:b]
                      str1 = "'" + a + "': [{id: '" + line[0:2] + "',text: '" + line[0:len(line) - 1] + "',highlight: '<strong>" + line[0:a1]+' '+line[a1+1:b] + "</strong>" + line[len(a)+1:-1] + "'}],"


                      # x+=1
                      file.write(str1)
                      # print('x'+str(x))
                      file.write('\n')
                  else :
                      a = line[0:b]
                      str1 = "'" + a + "': [{id: '" + line[0:2] + "',text: '" + line[0:len(line)-1] + "',highlight: '<strong>" + a + "</strong>" + line[len(a):-1] + "'}],"

                     # x+=1
                      file.write(str1)
                     # print('x'+str(x))
                      file.write('\n')

                  b += 1

                '''file.write("'{}': [".format(i))
                file.write("{")

                file.write(
                    "\nid: '{}',\ntext: '{}',\nhighlight: '<strong>{}</strong>{}'\n".format(pre, pre, i, pre[len(a):]))
                file.write("}],")'''

                #  else:
                #     str1 = "'" + i + "': [{id: '" + line[0:2] + "',text: '" + line[0:len(line)-1] + "',highlight: '<strong>" + line[1] + "</strong>" + line[2:-1] + "'}],"
                #
                #
                #     file.write(str1)
                #     file.write('\n')

                ''' file.write("'{}': [".format(i))

                file.write("{")

                file.write(
                    "\nid: '{}',\ntext: '{}',\nhighlight: '<strong>{}</strong>{}'\n".format(pre, pre, i, pre[1:]))
                file.write("}],")'''

              else:
                # a = line[0:b]
                # str1 = "'" + a + " ': [{id: '" + line[0:2] + "',text: '" + line[0:len(
                #       line) - 1] + "',highlight: '<strong>" + a + "</strong>" + line[len(a):-1] + "'}],"
                #
                # # x+=1
                # file.write(str1)
                # # print('x'+str(x))
                # file.write('\n')
                assaa+=1
                print('assaa'+str(assaa))
                b += 1


        if pre2!=None:

            b = 1
            print(pre2,'2')
            # pre2=str(pre2)
            for i in range(len(pre2.group(1))):
                print(pre2.group(1))
                print(i)
                if b >= 0:
                    a = pre2.group(1)[0:b]
                    str1 = "'" + a + "': [{id: '" + line[0:2] + "',text: '" + line[0:len(line)-1] + "',highlight: '<strong>" + a + "</strong>" + line[len(a):-1] + "'}],"

                    file.write(str1)
                    file.write('\n')
                    x+=1
                    print(str(x)+'x')
                    '''file.write("'{}': [".format(i))

                    file.write("{")

                    file.write(
                        "\nid: '{}',\ntext: '{}',\nhighlight: '<strong>{}</strong>{}'\n".format(pre, pre, i, pre[len(a):]))len(line)-1len(line)-1
                    file.write("}],")'''

                # else:
                #     str1 = "'" + pre2.group()[0] + "': [{id: '" + line[0:2] + "',text: '" + line[0:len(line)-1] + "',highlight: '<strong>" + line[0] + "</strong>" + line[1:-1] + "'}],"
                #
                #     file.write('x')
                #     file.write(str1)
                #     file.write('\n')

                ''' file.write("'{}': [".format(i))

                    file.write("{")

                    file.write(
                        "\nid: '{}',\ntext: '{}',\nhighlight: '<strong>{}</strong>{}'\n".format(pre, pre, i, pre[1:]))
                    file.write("}],")'''
                b = b + 1

    '''
        '夏目': [
                {
                    id: '夏目　漱石',
                    text: '夏目　漱石',
                    highlight: '<strong>夏目</strong>　漱石'
                }
                ],
                '''