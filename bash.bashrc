command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
}
PS1='\[\e[31m\]┌─[\[\e[37m\]\T\[\e[31m\]]─────\e[1;93m[root]\e[0;31m───[\#]\n|\n\e[0;31m└─[\[\e[31m\]\e[0;35m\W\[\e[31m\]]────►\e[1;92m'
clear
termux-tts-speak "welcome back  sunny"
sleep 0
mpv /$HOME/qurxin/sunny2.mp3
sleep 0
mpv /$HOME/qurxin/sunny10.mp3
termux-tts-speak "turning on the light"
termux-torch on
termux-tts-speak "turning off the light"
termux-torch off
termux-tts-speak "thank you shanni"

clear
echo -e "Created By \e[5mYahye shanni"
echo "----------------------------" | lolcat

echo "

 shanni " | lolcat
figlet 2.0 | lolcat
