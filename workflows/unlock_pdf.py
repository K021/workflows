#!/Users/jooeon/.pyenv/versions/3.12.8/envs/workflows/bin/python
from pathlib import Path
from typing import Optional
from pypdf import PdfReader, PdfWriter
import argparse


def remove_pdf_password(
    input_pdf: str,
    password: Optional[str] = None,
    output_pdf: Optional[str] = None,
):
    """암호화된 PDF의 암호를 제거하고 새로운 PDF로 저장하는 함수"""
    input_path = Path(input_pdf).absolute()
    output_pdf = output_pdf or input_path.stem + "_unlocked.pdf"
    output_path = input_path.parent / output_pdf

    print(f"📄 입력 PDF: {input_path}")
    print(f"💾 출력 PDF: {output_path}")

    if not input_path.exists():
        print(f"❌ 파일을 찾을 수 없습니다: {input_pdf}")
        return

    reader = PdfReader(input_path)

    if not password:
        password = input("🔒 PDF 암호를 입력하세요: ")

    # PDF 암호 해제
    if reader.is_encrypted:
        if not reader.decrypt(password):
            print("❌ 암호가 올바르지 않습니다.")
            return
        print("🔓 암호 해제 완료!")
    else:
        print("🔓 암호가 없는 PDF입니다.")

    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    # 새 PDF로 저장 (암호 없이)
    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"✅ 암호가 제거된 PDF가 저장되었습니다: {output_pdf}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="암호화된 PDF의 암호를 제거하고 새로운 PDF로 저장하는 스크립트"
    )
    parser.add_argument("input_pdf", help="암호화된 PDF 파일 경로")
    parser.add_argument("password", nargs="?", help="PDF 파일의 암호 (선택 사항)")
    parser.add_argument("output_pdf", nargs="?", help="암호가 제거된 새로운 PDF 파일 경로 (선택 사항)")

    args = parser.parse_args()

    remove_pdf_password(args.input_pdf, args.password, args.output_pdf)
