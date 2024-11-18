from setuptools import setup, find_packages

setup(
    name='Emguard',  # ชื่อแพ็กเกจของคุณ
    version='0.1.0',  # เวอร์ชันของแพ็กเกจ
    description='Virus Detection That use ember Dataset ',
    author='Jinnathit Chanpinit',
    author_email='jinnathit@gmail.com',
    url='https://github.com/Namikocat/Emguard-Virus-Detection',  # URL ไปยัง repo หรือเว็บไซต์ของคุณ
    packages=find_packages(),  # ค้นหาและเพิ่มแพ็กเกจทั้งหมดในโปรเจกต์
    install_requires=[
        'pandas',
        'jsonlines',
        'sklearn',
        'tensorflow',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',  # ระบุเวอร์ชัน Python ขั้นต่ำ
)
