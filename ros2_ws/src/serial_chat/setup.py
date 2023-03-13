from setuptools import setup

package_name = 'serial_chat'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sreeram3927',
    maintainer_email='sreeram292004@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'serial_node = serial_chat.serial_node:main',
            'chat_screen = serial_chat.chat_screen:main',
        ],
    },
)
