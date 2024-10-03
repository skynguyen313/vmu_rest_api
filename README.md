██    ██ ███    ███ ██    ██     ██████  ███████ ███████ ████████      █████  ██████  ██ 
██    ██ ████  ████ ██    ██     ██   ██ ██      ██         ██        ██   ██ ██   ██ ██ 
██    ██ ██ ████ ██ ██    ██     ██████  █████   ███████    ██        ███████ ██████  ██ 
 ██  ██  ██  ██  ██ ██    ██     ██   ██ ██           ██    ██        ██   ██ ██      ██ 
  ████   ██      ██  ██████      ██   ██ ███████ ███████    ██        ██   ██ ██      ██ 

1. Giới thiệu
2. Hướng dẫn
   2.1. Tạo môi trường ảo (virtual environment)
     $ python -m venv venv
     $ cd venv/
     $ cd scripts
     $ .\activate
   2.2. Kích hoạt môi trường venv
     Đi đến đường dẫn có chứa thư mục 'venv' thực hiện lệnh
     $ .\venv\Scripts\Activate.ps1
   2.3. Cài đặt các gói package
     Trong thưu mục dự án vmu_rest_api thực hiện lệnh
     $ pip install -r requirements.txt
     Hoặc muốn liệt kê tất cả các gói và phiên bản đã được cài đặt trong môi trường hiện tại, thực hiện lệnh
     $ pip freeze > requirements.txt
