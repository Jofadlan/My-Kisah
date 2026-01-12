import os
import sys

# --- Classes ---

class Ending:
    def __init__(self, nama, tipe, tercapai=False):
        self.nama = nama
        self.tipe = tipe
        self.tercapai = tercapai

class GameState:
    def __init__(self):
        self.player_name = ""
        self.affinity = 0
        self.conflict_flag = False
        self.broken_bond_flag = False

# --- Helper Functions ---

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tekan_enter():
    print("\n( Tekan Enter untuk melanjutkan )")
    input()

def get_valid_input(min_val, max_val):
    while True:
        try:
            choice = int(input("Pilih: "))
            if min_val <= choice <= max_val:
                return choice
            else:
                print(f"Pilihan tidak valid. \nMasukkan angka diantara {min_val} - {max_val}: ")
        except ValueError:
            print("Pilihan tidak valid. \nMasukkan angka: ")

def get_player_name(max_length):
    while True:
        name = input(f"Masukkan nama karaktermu: ")
        # Strip whitespace and check if empty
        name = name.strip()
        if len(name) > 0:
            if len(name) > max_length:
                print(f"Nama terlalu panjang (maksimal {max_length} karakter).")
                continue
            return name
        print("Nama tidak boleh kosong.")

def show_endings(endings):
    clear_screen()
    print("=== RIWAYAT ENDING ===\n")
    ada = False
    for ending in endings:
        if ending.tercapai:
            print(f" {ending.nama} [{ending.tipe}]")
            ada = True
    if not ada:
        print("Belum ada ending yang tercapai.")
    tekan_enter()

# --- Scene Functions ---

def play_cafe_scene(endings, state):
    clear_screen()
    print(" Malam itu kalian bertemu lagi di kafe langganan.")
    print(f" {state.player_name}, dan Silvia sudah lama saling kenal-namun belakangan ada sesuatu yang menggantung.")
    tekan_enter()

    clear_screen()
    print("Kamu melihat Silvia di pojok kafe. Dia tampak sendirian.")
    print("Apa yang akan kamu lakukan?")
    print("1. Datang dan sapa dengan hangat.")
    print("2. Duduk pelan di sampingnya, menunggu suasana santai.")
    print("3. Menunggu sampai dia memperhatikanmu lalu menyapa.")
    print("4. Terlihat gugup dan pergi dari kafe.")
    print("5. Kembali ke menu utama.")
    
    pilihan1 = get_valid_input(1, 5)
    
    if pilihan1 == 5:
        return False # Kembali ke menu utama

    if pilihan1 == 4:
        clear_screen()
        print("Kamu: (terlalu gugup, kamu memutuskan pergi tanpa bicara.)")
        print(" Hari-hari berikutnya komunikasi memudar. Silvia mulai menjauh.")
        print(f"\n--- Ending tercapai: {endings[4].nama} [{endings[4].tipe}] ---")
        endings[4].tercapai = True
        tekan_enter()
        return False # Cerita berakhir
    elif pilihan1 == 1:
        state.affinity += 2
        print("\nKamu mendekat dan menyapa dengan tenang.")
        print("Silvia: \"Oh, hai. Senang kamu mampir.\" (senyum tipis)")
        tekan_enter()
    elif pilihan1 == 2:
        state.affinity += 2
        print("\nKamu duduk perlahan di sampingnya, memberi ruang.")
        print("Silvia: \"Kamu baik-baik saja?\" (suara lembut)")
        tekan_enter()
    else: # Option 3
        print("\nKamu menunggu momen. Saat dia menoleh, kamu tersenyum.")
        print("Silvia: \"Oh, akhirnya kamu datang juga.\" (pelan)")
        tekan_enter()
    
    return True # Lanjut ke scene berikutnya

def play_conversation_scene(endings, state):
    clear_screen()
    print("Kalian mulai berbincang. Pilih bagaimana gaya bicaramu.")
    print("1. Cerita ringan tentang kerja / kegiatan.")
    print("2. Tanyakan bagaimana perasaannya akhir-akhir ini.")
    print("3. Goda dengan bercanda.")
    print("4. Menyinggung hal yang sensitif di masa lalu.")
    print("5. Kembali ke menu utama.")

    pilihan2 = get_valid_input(1, 5)
    if pilihan2 == 5:
        return False

    if pilihan2 == 1:
        state.affinity += 2
        print("\nKamu: \"Kerjaan belakangan gimana?\" ")
        print("Silvia: \"Lumayan sibuk, tapi senang ada yang nemenin.\" (tersenyum)")
        tekan_enter()
    elif pilihan2 == 2:
        state.affinity += 1
        print("\nKamu menanyakan hal personal dengan hati-hati.")
        print("Silvia: \"Kadang capek, tapi aku baik kok. Makasih udah nanya.\" ")
        tekan_enter()
    elif pilihan2 == 3:
        state.affinity += 1
        print("\nKamu menggoda Silvia soal minuman yang dia pesan.")
        print("Silvia: (tersipu) \"Dasar.\", namun terlihat hangat.")
        tekan_enter()
    else: # Option 4
        state.affinity -= 3
        state.conflict_flag = True
        print("\nKamu menyentuh topik lama yang jelas menyakitinya.")
        print("Silvia: \"Kenapa kamu harus bawa itu lagi?\" Suaranya meninggi.")
        tekan_enter()

        clear_screen()
        print("Percakapan memanas. Pilih responsmu:")
        print("1. Minta maaf dan tarik kata-katamu.")
        print("2. Tetap bersikap defensif dan membela dirimu.")
        print("3. Coba ubah topik dan bersikap tenang.")
        print("4. Kembali ke menu utama.")

        pilihan_conflict = get_valid_input(1, 4)
        if pilihan_conflict == 4:
            return False

        if pilihan_conflict == 1:
            state.affinity += 1
            state.conflict_flag = False
            print("\nKamu: \"Maaf, aku keterusan. Aku nggak bermaksud nyakitin.\" ")
            print("Silvia: (menarik napas) \"Ya udah... kita lanjut aja.\"")
            tekan_enter()
        elif pilihan_conflict == 2:
            state.affinity -= 2
            state.conflict_flag = True
            state.broken_bond_flag = True
            print("\nKamu bersikap defensif. Silvia terlihat sangat terluka dan berdiri.")
            print("Silvia: \"Aku butuh waktu.\" (lalu pergi dari meja)")
            tekan_enter()
        else: # Option 3
            print("\nKamu mencoba meredam suasana dengan hati-hati.")
            print("Silvia: \"Baiklah... kita bicara lain kali.\" (nada dingin)")
            tekan_enter()
            
    return True

def play_conflict_scene(endings, state):
    clear_screen()
    print("Beberapa hari setelah kejadian di kafe, suasana benar-benar berubah.")
    print("Kalian tetap bertemu beberapa kali, namun ada jarak yang tak hilang.")
    print(" Suatu malam kalian akhirnya bertemu untuk bicara satu kali lagi.")
    tekan_enter()

    clear_screen()
    print(f"{state.player_name}: \"Yaudah ya, kenapa lu menjauh?\"")
    print("Silvia: \"Gw ga menjauh, gw ga menjauh.\"")
    print(f"{state.player_name}: \"Yaudah...\"")
    print("Silvia: \"Melihat dari apa-apa yang sudah lalu aja, gw ga mau nyakitin diri gw sendiri.\"")
    print(f"{state.player_name}: \"Nggak, gw udah nggak kayak dulu lagi. Gw udah berubah.\"")
    print("Silvia: \"Ok kalo lu udah berubah, bagus. Tapi rasa sakit yang gue rasain dulu masih ada.\"")
    print(f"{state.player_name}: \"Nggak, gw ga akan ngebuat rasa sakit itu terulang kembali, Sil.\"")
    print("Silvia: \"Yaudah ok ok... kalo lu ga bakal melakukan itu yaudah ok.\"")
    print(f"{state.player_name}: \"Yaudah, trus gw juga udah ok, maksud gw kenapa lu?\"")
    print("Silvia: \"Udah! Stop! Stop! Ya udah! Kan katanya lu baik. Ya udah. Kalau gitu diem di sini.\"")
    print(f"{state.player_name}: \"Ya kenapa? Kenapa lu takut sama orang baik?\"")
    print("Silvia: \"Lu itu hak gue. Kalau gue pengen pergi juga hak gue. Kenapa lu memaksakan kehendak gue?\"")
    print(f"{state.player_name}: \"Tapi kan... Gue kan enggak jahat sama lu.\"")
    print("Silvia: \"(tertawa sarkas) Lu enggak jahat? Lu udah berapa kali buat gw hancur. Tapi ya udah, kalo lu sekarang baik, bagus. Tapi rasa sakit yang gw rasain itu masih ada.\"")
    print(f"{state.player_name}: \"Tapi-\"")
    print("Silvia: \"Jadi ya udah, gue pengen pergi aja.\"")
    print(f"{state.player_name}: \"Tapi kan gue pengen benerin itu semua. Gue sekarang pengen benerin itu semua.\"")
    print("Silvia: \"Ga Bisa!\"")
    print(f"{state.player_name}: \"Bisa!\"")
    print("Silvia: \"Ga Bisa! Ga Bisa!\"")
    print(f"{state.player_name}: \"Bisa! Bisa!\"")
    print("Silvia: \"Ga... ga bisa...\"")
    print("\n Retakan itu sulit disatukan kembali. Kalian berpisah dengan banyak penyesalan.")
    print(f"\n--- Ending tercapai: {endings[3].nama} [{endings[3].tipe}] ---")
    endings[3].tercapai = True
    tekan_enter()
    return False

def play_honest_moment_scene(endings, state):
    clear_screen()
    print("Momen tenang muncul. Kamu rasakan kesempatan untuk lebih jujur.")
    print("Pilih cara kamu mempersiapkan diri sebelum mengatakannya:")
    print("1. Rangkul kehangatan suasana, mulai dengan pujian sederhana.")
    print("2. Ceritakan sesuatu yang rentan dari dirimu dulu.")
    print("3. Terlihat ragu dan sering terdiam.")
    print("4. Bercanda berlebihan untuk menutupi perasaan.")
    print("5. Kembali ke menu utama.")

    pilihan3 = get_valid_input(1, 5)
    if pilihan3 == 5:
        return False

    if pilihan3 == 1:
        state.affinity += 3
        print("\nKamu: \"Malam ini kamu terlihat tenang. Aku senang bisa di sini.\" ")
        print("Silvia: (tersenyum lembut) \"Iya... aku juga.\"")
        tekan_enter()
    elif pilihan3 == 2:
        state.affinity += 2
        print("\nKamu menceritakan masa sulit yang membuatmu berubah.")
        print("Silvia: \"Terima kasih sudah percaya sama aku.\" (mata berkaca)")
        tekan_enter()
    elif pilihan3 == 3:
        state.affinity -= 1
        print("\nKamu terlihat ragu, sering menunduk. Kesempatan terasa samar.")
        tekan_enter()
    else: # Option 4
        state.affinity -= 1
        print("\nKamu bercanda berlebihan. Silvia terlihat tidak yakin seberapa serius kamu.")
        tekan_enter()
        
    return True

def play_confession_scene(endings, state):
    clear_screen()
    print("Sekarang momen itu datang. Apakah kamu akan menyatakan perasaanmu?")
    print("1. Ya")
    print("2. Tidak")
    print("3. Kembali ke menu utama.")

    pilih_confess = get_valid_input(1, 3)
    if pilih_confess == 3:
        return False

    if pilih_confess == 2:
        clear_screen()
        print("Kamu memutuskan untuk tidak mengatakannya. Hubungan tetap sebagai teman.")
        print(f"Silvia: \"{state.player_name}, makasih ya. Kamu selalu ada.\"")
        print(f"\n--- Ending tercapai: {endings[1].nama} [{endings[1].tipe}] ---")
        endings[1].tercapai = True
        tekan_enter()
        return False

    clear_screen()
    print(f"{state.player_name}: \"Aku tidak akan bisa sampai sejauh ini tanpa kamu. Terima kasih ya.\"")
    print("Silvia: \"Kenapa tiba-tiba lo? Lo bikin malu aja lo.\"")
    print(f"{state.player_name}: \"Aku memang kayak gini. Aku nggak pernah punya seseorang yang kerja bareng dan saling dukung seperti ini.\"")
    print(f"{state.player_name}: \"Setelah kenal sama kamu, aku sadar aku nggak sebebas dulu. Aku berubah karena kehadiranmu.\"")
    print("Silvia: \"Kenapa sih lo tiba-tiba ngomong gitu?\"")
    print(f"{state.player_name}: \"Maaf, agak terbawa suasana.\"")
    print("Silvia: \"Aku juga... kadang merasa sendiri. Ada yang melindungi aku, ada yang aku lindungi. Tapi aku jarang menemukan yang seimbang.\"")
    print("Silvia: \"Saat aku ketemu kamu, aku sadar aku kesepian sebelumnya.\"")
    tekan_enter()

    clear_screen()
    if state.affinity >= 7:
        print("Silvia tersenyum, wajahnya memerah.")
        print("Silvia: \"T-Ta-Tapi gue pengen denger dulu, menurut lo ini gue terlihat gimana malam ini?\"")
        print(f"{state.player_name}: \"Malam ini lo terlihat sangat cantik, Sil. Serius.\" ")
        print("Silvia: (tersipu, canggung bahagia)")
        print(f"{state.player_name}: \"Nah berarti gue ganteng apa nggak?\"")
        print("Silvia: \"Iya... Iya bang... iya kok iya.\"")
        print("\n Malam itu menjadi awal yang baru. Kalian memulai hubungan dengan hangat.")
        print(f"\n--- Ending tercapai: {endings[0].nama} [{endings[0].tipe}] ---")
        endings[0].tercapai = True
    else:
        print("Silvia menunduk, suaranya lembut.")
        print(f"Silvia: \"{state.player_name}... maaf. Aku senang kamu jujur, tapi aku merasa kita lebih cocok sebagai teman.\"")
        print(f"{state.player_name}: \"Aku ngerti... kalau begitu aku akan tetap di sisimu sebagai teman.\"")
        print(f"\n--- Ending tercapai: {endings[2].nama} [{endings[2].tipe}] ---")
        endings[2].tercapai = True
    tekan_enter()
    return False

def play_story(endings, state):
    # Reset state for new game
    state.affinity = 0
    state.conflict_flag = False
    state.broken_bond_flag = False

    if not play_cafe_scene(endings, state): return
    if not play_conversation_scene(endings, state): return
    
    if state.broken_bond_flag:
        play_conflict_scene(endings, state)
        return
        
    if not play_honest_moment_scene(endings, state): return
    play_confession_scene(endings, state)

# --- Main ---

def main():
    # Initialize Endings
    endings = [
        Ending("Heart Connected", "Happy Ending"),
        Ending("Unspoken Feelings", "True Ending"),
        Ending("Friendzone", "True Ending"),
        Ending("Broken Bonds", "Sad Ending"),
        Ending("Faded Away", "Sad Ending")
    ]

    state = GameState()

    while True:
        clear_screen()
        print("====================")
        print("   \"My Kisah\" ")
        print("====================")
        print("1. Main Cerita")
        print("2. Lihat Riwayat Ending")
        print("3. Keluar")
        
        menu = get_valid_input(1, 3)

        if menu == 1:
            state.player_name = get_player_name(50)
            play_story(endings, state)
        elif menu == 2:
            show_endings(endings)
        elif menu == 3:
            clear_screen()
            print("Terima kasih telah bermain. Sampai jumpa.")
            tekan_enter()
            sys.exit()

if __name__ == "__main__":
    main()
