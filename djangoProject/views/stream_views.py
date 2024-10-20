import os
from wsgiref.util import FileWrapper

from django.http import StreamingHttpResponse

def stream_music(request):
    file_path = request.GET.get("path")

    wrapper = FileWrapper(open(file_path, 'rb'))

    response = StreamingHttpResponse(wrapper, content_type='audio/mp3')

    # 设置头部信息，推荐使用原始文件名，防止中文乱码
    response['Content-Length'] = os.path.getsize(file_path)

    return response