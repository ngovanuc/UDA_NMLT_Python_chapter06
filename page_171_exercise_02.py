"""
author : Ngô Văn Úc
date: 30/08/2021
program: 2. Describe the processes of top-down design and stepwise refinement. Where does
the design start, and how does it proceed
solution:
    - trong một chương trình nếu thiệt kế và thực hiện theo hàm main
    thì việc đầu tiên cần phận định được vấn đề có thể chia ra mấy giai đoạn xử lí và nhiệm vụ
    cho mỗi giai đoạn là gì, yêu cầu sau khi kết thúc từng bước sẽ có kết quả để thực hiện các
    vấn đề khác.
    - có hai phương án thiết kế hàm main: đó là theo kiểu từ trên xuống hoặc từ dưới lên
    - từ trên xuống: bản thân mình thấy cách này dễ hơn, khi mà nó từ vấn đề lớn nhất và mổ xẻ ra thành các vấn đề nhỏ
    và từng quy trình được thực hiện một cách chính xác và tỉ mỉ
    - từ dưới lên: cách này có vẻ khó hơn khi mà chúng ta đi từ vấn đề nhỏ để cấu tạo thành một vấn đề lớn và đưa ra được
    kết quả tốt
    - ví dụ: nếu trong chương trình tạo câu ở chương 4 theo cách hai có thể sẽ khó hơn một chút nhưng
    theo cách thứ nhất thì sẽ dế dàng hơn và dễ đọc hơn. khi mà chúng ta biết được quy tắc tạo câu, trong một câu gồm có nhiều thành
    phần thì lại được chia ra các vấn đề con như câu thì có chủ ngữ vị ngữ, trong vị ngữ lại có một cụm động từ hoặc danh từ hoặc trạng thái
    từ mỗi cụm động từ hoặc trạng thái đó chúng ta lại chia các vấn đề nhỏ hơn như là động từ, từ nối và động từ........
    từ các nhiệm vụ đó rõ ràng chúng ta phải biết cách để cấu tạo thành một cụm bằng quy tắc và từ điển và cách chọn từ trong từ điển


"""
