from UI import UI_view



def creat_html():
    first_name, lats_name, phone_number = UI_view()
    style = 'style="font-size; 30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '     <p {}> Имя: {} </p>\n' \
            .format(style, first_name)
    html += '     <p {}> Фамилия: {} </p>\n' \
        .format(style, lats_name)
    html += '     <p {}> Номер телефона: {} </p>\n' \
        .format(style, phone_number)
    html += '   </body>\n<html>'


    with open('index.html', 'w', encoding='CP1251') as page:
        page.write(html)
    return html