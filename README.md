# vk_audio.py
Mobile-API for [vkontakte](https://vk.com) audio api

## Examples
```python3
import vk_audio
VkAudioClient = vk_audio.VkAudioClient(access_token="")
popular_audios = VkAudioClient.get_popular_audios(count=100)
print(popular_audios)
```
