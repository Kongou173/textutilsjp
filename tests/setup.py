from setuptools import setup, find_packages

setup(
    name="textutilsjp",
    version="0.2.0",
    description="日常で役立つ日本語テキスト整形・抽出・要約・解析ツール集",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourname/textutilsjp",
    packages=find_packages(),
    install_requires=[
        # 'jaconv',  # 必要に応じてコメントアウトを外してください
    ],
    python_requires='>=3.7',
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
