import pygame


def file_records():
    try:
        with open('record') as record_file:
            record = record_file.read()
    except FileNotFoundError:
        with open('record', 'w') as record_file:
            record_file.write('1')
            record_file.close()
        with open('record', 'r') as record_file:
            record = record_file.read()
    return record


intt = int(file_records())

print(intt + 1)

image = pygame.image.load('ship.bmp')
image_rect = image.get_rect()
print(image_rect)
