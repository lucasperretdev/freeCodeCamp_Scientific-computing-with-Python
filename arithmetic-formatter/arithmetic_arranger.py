# def arithmetic_arranger(problems, answer):
# return arranged_problems

inputTest = ["44 + 8115", "909 - 2", "45 + 43",
             "123 + 49", "888 + 40"]
dosum = True


def arithmetic_arranger(problems, dosum=None):

    data_list = list()
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""

    for item in problems:
        data_clean = dict()
        array = item.split(" ")
        first_number = array[0]
        operator = array[1]
        second_number = array[2]
        # création d'une list avec dictionnaire
        data_clean['first'] = first_number
        data_clean['operator'] = operator
        data_clean['second'] = second_number
        data_list.append(data_clean)

    list_for_max = list()

    for item in data_list:
        list_for_max.append(
            max((len(item['first'])+2), (len(item['second'])+2)))

    # check for errors
    if len(data_list) > 5:
        return 'Error: Too many problems.'

    for item in data_list:
        if item['operator'] != "+" and item['operator'] != '-':
            return "Error: Operator must be '+' or '-'."
        else:
            pass

    for item in data_list:
        try:
            int(item['first'])
            int(item['second'])
        except:
            return 'Error: Numbers must only contain digits.'

    for item in data_list:
        if len(item['first']) > 4 or len(item['second']) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    # convert into the right format
    i = 0
    for i in range(len(data_list)):
        data_list[i]['first']
        first_line += ((list_for_max[i] - len(data_list[i]['first']))
                       * " ")+data_list[i]['first'] + "    "

        if len(data_list[i]['first']) >= len(data_list[i]['second']):
            diff = len(data_list[i]['first']) - len(data_list[i]['second'])
            second_line += data_list[i]['operator'] + \
                " " + " "*diff+data_list[i]['second']+"    "
        else:
            second_line += data_list[i]['operator'] + \
                " "+data_list[i]['second']+"    "

        third_line += "-"*list_for_max[i]+"    "

        sum = ""

        if data_list[i]['operator'] == '+':
            sum = str((int(data_list[i]['first']) +
                       int(data_list[i]['second'])))
            fourth_line += " "*(list_for_max[i]-len(sum))+sum+"    "
        else:
            sum = str((int(data_list[i]['first']) -
                       int(data_list[i]['second'])))
            fourth_line += " "*(list_for_max[i]-len(sum))+sum+"    "

    if dosum == True:
        final_string = first_line.rstrip()+'\n' + \
            second_line.rstrip()+'\n'+third_line.rstrip()+'\n'+fourth_line.rstrip()

    else:
        final_string = first_line.rstrip()+'\n' + \
            second_line.rstrip()+'\n'+third_line.rstrip()

    return final_string


print(arithmetic_arranger(inputTest, True))
