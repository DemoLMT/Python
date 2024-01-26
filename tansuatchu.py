def dem_tan_suat(s):
    s = s.lower()
    tan_suat = {}
    for char in s:
        if char.isalnum():
            if char in tan_suat:
                tan_suat[char] += 1
            else:
                tan_suat[char] = 1
    tan_suat = dict(sorted(tan_suat.items()))
    for key, value in tan_suat.items():
        print(key, value)
s = input()
dem_tan_suat(s)
