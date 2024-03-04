import datetime

from putting_it_together.chapter7 import create_image


def main():  # pragma: no cover
    image = create_image()

    with open('../images/chapter8.ppm', 'w', encoding="ascii") as f:
        for line in image.to_ppm():
            f.write(line)


if __name__ == '__main__':  # pragma: no cover
    start = datetime.datetime.now()
    main()
    print(f"{datetime.datetime.now() - start}")
