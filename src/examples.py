import vkAudio
VkAudioClient = vkaudio.VkAudioClient(access_token="")
popular_audios = VkAudioClient.get_popular_audios(count=100)
print(popular_audios)
