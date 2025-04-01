#!/Users/jooeon/.pyenv/versions/3.12.8/envs/workflows/bin/python
from PIL import Image

def merge_images_grid(image_paths, rows, cols, output_path='output.jpg'):
    if len(image_paths) != rows * cols:
        raise ValueError(f"이미지 수가 {rows}x{cols} 격자에 맞지 않습니다.")

    # 이미지 열기
    images = [Image.open(p) for p in image_paths]

    # 모든 이미지 사이즈 통일 (첫 번째 이미지 기준)
    width, height = images[0].size
    images = [img.resize((width, height)) for img in images]

    # 새 캔버스 만들기
    merged_width = width * cols
    merged_height = height * rows
    new_img = Image.new('RGB', (merged_width, merged_height), color='white')

    # 이미지 배치
    for idx, img in enumerate(images):
        row = idx // cols
        col = idx % cols
        new_img.paste(img, (col * width, row * height))

    new_img.save(output_path)
    print(f"저장 완료: {output_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="이미지를 격자 형태로 합치는 스크립트")
    parser.add_argument("image_paths", nargs='+', help="합칠 이미지 파일 경로들")
    parser.add_argument("-r", "--rows", type=int, required=True, help="행 수")
    parser.add_argument("-c", "--cols", type=int, required=True, help="열 수")
    parser.add_argument("-o", "--output", type=str, default='output.jpg', help="출력 파일 경로")

    args = parser.parse_args()

    merge_images_grid(args.image_paths, args.rows, args.cols, args.output)