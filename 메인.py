{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOXWOfwexS4KpHI3hboXq4M",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/tunip0067/NLP_2023/blob/main/%EB%A9%94%EC%9D%B8.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "nwtfvBOkICPw"
      },
      "outputs": [],
      "source": [
        "from gtts import gTTS\n",
        "from pydub import AudioSegment\n",
        "from pydub.playback import play\n",
        "import random, os\n",
        "\n",
        "os.makedirs('samples', exist_ok=True)\n",
        "os.makedirs('result', exist_ok=True)\n",
        "\n",
        "string = '안녕하세요 너굴 상회입니다'\n",
        "random_factor = 0.35\n",
        "\n",
        "result_sound = None\n",
        "\n",
        "for i, letter in enumerate(string):\n",
        "    if letter == ' ':\n",
        "        new_sound = letter_sound._spawn(b'\\x00' * (44100 // 3), overrides={'frame_rate': 44100})\n",
        "        new_sound = new_sound.set_frame_rate(44100)\n",
        "    else:\n",
        "        if not os.path.isfile('samples/%s.mp3' % letter):\n",
        "            tts = gTTS(letter, lang='ko')\n",
        "            tts.save('samples/%s.mp3' % letter)\n",
        "\n",
        "        letter_sound = AudioSegment.from_mp3('samples/%s.mp3' % letter)\n",
        "\n",
        "        raw = letter_sound.raw_data[5000:-5000]\n",
        "\n",
        "        octaves = 2.0 + random.random() * random_factor\n",
        "        frame_rate = int(letter_sound.frame_rate * (2.0 ** octaves))\n",
        "        print('%s - octaves: %.2f, fr: %.d' % (letter, octaves, frame_rate))\n",
        "\n",
        "        new_sound = letter_sound._spawn(raw, overrides={'frame_rate': frame_rate})\n",
        "        new_sound = new_sound.set_frame_rate(44100)\n",
        "\n",
        "    result_sound = new_sound if result_sound is None else result_sound + new_sound\n",
        "\n",
        "play(result_sound)\n",
        "result_sound.export('result/%s.mp3' % string, format='mp3')"
      ]
    }
  ]
}