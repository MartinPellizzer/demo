from PIL import Image, ImageDraw, ImageFont

vault_folderpath = 'C:/vault'
fonts_folderpath = f'{vault_folderpath}/fonts'

a4_w = 2480
a4_h = 3508

ml = 300
mt = 500
mr = 500
mb = 800

text_area_x1 = ml
text_area_y1 = mt
text_area_x2 = a4_w - mr
text_area_y2 = a4_h - mb
text_area_w = text_area_x2 - text_area_x1
text_area_h = text_area_y2 - text_area_y1

col_num = 2
col_w = text_area_w / col_num

row_num = 4
row_h = text_area_h / row_num

line_num = 13
line_spacing = 1.3
line_h = row_h / line_num

font_size = line_h / line_spacing
font = ImageFont.truetype(f'{fonts_folderpath}/helvetica/Helvetica.ttf', font_size)

img = Image.new('RGB', (a4_w, a4_h), '#ffffff')
draw = ImageDraw.Draw(img)

if 0:
    for i in range(row_num):
        for j in range(line_num+1):
            draw.line((text_area_x1, text_area_y1 + row_h*i + line_h*j, text_area_x2, text_area_y1 + row_h*i + line_h*j), fill='#00ff00', width=4)

    for i in range(col_num+1):
        draw.line((text_area_x1 + col_w*i, text_area_y1, text_area_x1 + col_w*i, text_area_y2), fill='#00ffff', width=4)
        draw.line((text_area_x1 + col_w*i - line_h, text_area_y1, text_area_x1 + col_w*i - line_h, text_area_y2), fill='#00ffff', width=4)

    for i in range(row_num+1):
        draw.line((text_area_x1, text_area_y1 + row_h*i, text_area_x2, text_area_y1 + row_h*i), fill='#00ffff', width=4)
        draw.line((text_area_x1, text_area_y1 + row_h*i - line_h, text_area_x2, text_area_y1 + row_h*i - line_h), fill='#00ffff', width=4)

with open('body-text.txt', encoding='utf-8') as f: body_text = f.read()
body_text = body_text.strip().replace('\n', ' ').replace('  ', ' ')

lines = []
line = ''
for word in body_text.split(' '):
    _, _, line_w, _ = font.getbbox(line)
    _, _, word_w, _ = font.getbbox(word)
    if line_w + word_w < col_w - line_h:
        line += f'{word} '
    else:
        lines.append(line.strip())
        line = f'{word} '
lines.append(line.strip())

line_x = text_area_x1
line_y = text_area_y1
i = 0
for line in lines:
    draw.text((line_x, line_y + font_size*i*line_spacing), line, '#000000', font=font)
    i += 1

line_x = text_area_x1 + col_w
line_y = text_area_y1
i = 0
for line in lines:
    draw.text((line_x, line_y + font_size*i*line_spacing), line, '#000000', font=font)
    i += 1


draw.line((text_area_x1, text_area_y1, text_area_x2, text_area_y1), fill='#ff0000', width=4)
draw.line((text_area_x1, text_area_y2, text_area_x2, text_area_y2), fill='#ff0000', width=4)
draw.line((text_area_x1, text_area_y1, text_area_x1, text_area_y2), fill='#ff0000', width=4)
draw.line((text_area_x2, text_area_y1, text_area_x2, text_area_y2), fill='#ff0000', width=4)

img.save('output.jpg')
img.show()