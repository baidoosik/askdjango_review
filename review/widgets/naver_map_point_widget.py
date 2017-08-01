import re
from django import forms
from django.conf import settings # django.conf.global_settings + project.settings
from  django.template.loader import render_to_string

class NaverMapPointWidget(forms.TextInput):
    BASE_LAT, BASE_LNG = '37.497921', '127.027636'  # 강남역

    def render(self, name, value, attrs=None):
        width = str(self.attrs.get('width',800))
        height = str(self.attrs.get('height',600))
        if width.isdigit(): width + 'px'
        if height.isdigit(): height +'px'

        context = {'naver_client_id': settings.NAVER_CLIENT_ID,
                   'id': attrs['id'],  # 현재 formfield의 html id
                   'width': width, 'height': height,
                   'base_lat': self.BASE_LAT, 'base_lng': self.BASE_LNG}

        if value:
            try:
                lng, lat = re.findall(r'[+-]?[\d\.]+', value)
                context.update({'base_lat': lat, 'base_lng': lng})
            except (IndexError, ValueError):
                pass
        attrs['readonly'] = 'readonly' #앍가 전용 ,자바스크립트로만 수정가능
        parent_html = super().render(name, value, attrs)
        html = render_to_string('widget/naver_map_point_widget.html', context)

        return parent_html + html



