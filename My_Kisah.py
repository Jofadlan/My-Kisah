import os
import sys
import json

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
            print(f"Pilihan tidak valid. Masukkan angka diantara {min_val} - {max_val}")

def get_player_name(current_name, max_length):
    # Update prompt to show current name if it exists
    prompt = "Masukkan nama karaktermu: "
    if current_name:
        prompt = f"Masukkan nama karaktermu [{current_name}]: "
        
    while True:
        name = input(prompt)
        # Strip whitespace
        name = name.strip()
        
        # If input is empty and we have a saved name, keep the saved name
        if len(name) == 0 and current_name:
            return current_name
            
        if len(name) > 0:
            if len(name) > max_length:
                print(f"Nama terlalu panjang (maksimal {max_length} karakter).")
                continue
            return name
        print("Nama tidak boleh kosong.")

def show_endings(endings, player_name):
    clear_screen()
    print("=== RIWAYAT ENDING ===")
    if player_name:
        print(f"Pemain Terakhir: {player_name}")
    print()
    ada = False
    for ending in endings:
        if ending.tercapai:
            print(f" {ending.nama} [{ending.tipe}]")
            ada = True
    if not ada:
        print("Belum ada ending yang tercapai.")
    tekan_enter()

# --- Save & Load Functions ---

def save_progress(endings, player_name):
    data = {
        "player_name": player_name,
        "endings": [
            {"nama": e.nama, "tipe": e.tipe, "tercapai": e.tercapai} 
            for e in endings
        ]
    }
    try:
        with open("my_kisah_save.json", "w") as f:
            json.dump(data, f)
    except Exception as e:
        print(f"Error saving game: {e}")

def load_progress():
    try:
        if not os.path.exists("my_kisah_save.json"):
            return None, []
        with open("my_kisah_save.json", "r") as f:
            data = json.load(f)
            return data.get("player_name", ""), data.get("endings", [])
    except Exception as e:
        print(f"Error loading game: {e}")
        return None, []

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
        print("(terlalu gugup, kamu memutuskan pergi tanpa bicara.)")
        print(" Hari-hari berikutnya komunikasi memudar. Silvia mulai menjauh.")
        tekan_enter()
        clear_screen()
        print(" Akhirnya, hubungan kalian berakhir tanpa kata-kata.")
        print(" Waktu berlalu, dan kenangan itu perlahan memudar.") 
        print(f"\n--- Ending tercapai: {endings[4].nama} [{endings[4].tipe}] ---")
        endings[4].tercapai = True
        tekan_enter()
        return False # Cerita berakhir
    elif pilihan1 == 1:
        state.affinity += 2
        clear_screen()
        print("\nKamu mendekat dan menyapa dengan tenang.")
        print(f"{state.player_name}: \"Hai Silvia, lama nggak ketemu!\" ")
        tekan_enter()
        clear_screen()
        print("Silvia: \"Oh, hai. Senang kamu mampir.\" (senyum tipis)")
        tekan_enter()
    elif pilihan1 == 2:
        state.affinity += 2
        clear_screen()
        print("\nKamu duduk perlahan di sampingnya, memberi ruang.")
        print(f"{state.player_name}: \"Hai, aku harap aku nggak mengganggu.\" ")
        tekan_enter()
        clear_screen()
        print("\nSilvia menoleh, sedikit terkejut tapi tersenyum.")
        print("Silvia: \"Kamu baik-baik saja?\" (suara lembut)")
        tekan_enter()
    else: # Option 3
        clear_screen()
        state.affinity += 1
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
        state.affinity += 1
        clear_screen()
        print("\nKamu memulai dengan topik ringan tentang pekerjaan.")
        print(f"\n{state.player_name} \"Kerjaan belakangan gimana?\" ")
        tekan_enter()
        clear_screen()
        print("Silvia: \"Lumayan sibuk, tapi senang ada yang nemenin.\" (tersenyum)")
        tekan_enter()
    elif pilihan2 == 2:
        state.affinity += 1
        clear_screen()
        print("\nKamu menanyakan hal personal dengan hati-hati.")
        print(f"\n{state.player_name} \"Gimana perasaan kamu akhir-akhir ini?\" ")
        tekan_enter()
        clear_screen()
        print("Silvia: \"Kadang capek, tapi aku baik kok. Makasih udah nanya.\" ")
        tekan_enter()
    elif pilihan2 == 3:
        state.affinity += 2
        clear_screen()
        print("\nKamu menggoda Silvia soal minuman yang dia pesan.")
        print(f"{state.player_name} \"Kamu yakin mau pesen itu? Aku pikir kamu suka yang manis-manis.\" ")
        tekan_enter()
        clear_screen()
        print("Silvia: (tersipu) \"Dasar.\", namun terlihat hangat.")
        tekan_enter()
    else: # Option 4
        state.affinity -= 3
        state.conflict_flag = True
        clear_screen()
        print("\nKamu menyentuh topik lama yang jelas menyakitinya.")
        print(f"{state.player_name} \"Ingat nggak waktu itu pas kamu... ?\" ")
        tekan_enter()
        clear_screen()
        print("Silvia: \"Kenapa kamu harus bawa itu lagi sih ??!!\" Suaranya meninggi.")
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
            clear_screen()
            print(f"{state.player_name} \"Maaf, aku keterusan. Aku nggak bermaksud nyakitin.\" ")
            tekan_enter()
            clear_screen()
            print("Silvia: (menarik napas) \"Ya udah... kita lanjut aja.\"")
            tekan_enter()
        elif pilihan_conflict == 2:
            state.affinity -= 2
            state.conflict_flag = True
            state.broken_bond_flag = True
            clear_screen()
            print("\nKamu bersikap defensif. Silvia terlihat sangat terluka dan berdiri.")
            print(f"{state.player_name} \"Aku cuma jujur! Kenapa kamu bawa-bawa perasaan segala!\" ")
            tekan_enter()
            clear_screen()
            print("Silvia: \"Aku butuh waktu.\" (lalu pergi dari meja)")
            tekan_enter()
        else: # Option 3
            state.affinity -= 1
            state.conflict_flag = False
            clear_screen()
            print("\nKamu mencoba meredam suasana dengan hati-hati.")
            print(f"{state.player_name} \"Maaf ya, aku nggak maksud gitu. Jadi, ?\" ")
            tekan_enter()
            clear_screen()
            print("Silvia: \"Ok.\" (nada dingin)")
            tekan_enter()
            
    return True

def play_conflict_scene(endings, state):
    clear_screen()
    print("Beberapa hari setelah kejadian di kafe, suasana benar-benar berubah.")
    print("Kalian tetap bertemu beberapa kali, namun ada jarak yang tak hilang.")
    tekan_enter()
    clear_screen()
    print("Silvia tampak menghindar, dan percakapan menjadi singkat dan kaku.")
    print("Kamu merasa ada retakan yang sulit diperbaiki.")
    tekan_enter()
    clear_screen()
    print(" Suatu malam kalian akhirnya bertemu untuk bicara satu kali lagi.")
    print(f"{state.player_name}: \"Sil, kita perlu bicara.\"")
    tekan_enter()
    clear_screen()
    print("Silvia: \"Gw sibuk.\"")
    tekan_enter()
    clear_screen()
    print(f"{state.player_name}: \"Tolong... ini penting.\"")
    tekan_enter()
    clear_screen()
    print("Silvia: \"Ya udah, ngomong aja cepat.\"")
    print("Silvia terlihat tegang dan siap untuk pergi kapan saja.")
    tekan_enter()
    clear_screen()
    print(f"{state.player_name}: \"Kenapa lu kayak menjauh gitu sih??\"")
    tekan_enter()
    clear_screen()
    print("Silvia: \"Gw ga menjauh, lu aja yang maksa.\"")
    tekan_enter()
    clear_screen()
    print(f"{state.player_name}: \"Yaudah ya, kenapa lu menjauh?\"")
    tekan_enter()
    clear_screen()
    print("Silvia: \"Gw ga menjauh, gw ga menjauh.\"")
    tekan_enter()
    clear_screen()
    print(f"{state.player_name}: \"Yaudah...\"")
    tekan_enter()
    clear_screen()
    print("Silvia: \"Melihat dari apa-apa yang sudah lalu aja, gw ga mau nyakitin diri gw sendiri.\"")
    tekan_enter()
    clear_screen()
    print(f"{state.player_name}: \"Nggak, gw udah nggak kayak dulu lagi. Gw udah berubah.\"")
    tekan_enter()
    clear_screen()
    print("Silvia: \"Ok kalo lu udah berubah, bagus. Tapi rasa sakit yang gue rasain dulu masih ada.\"")
    tekan_enter()
    clear_screen()
    print(f"{state.player_name}: \"Nggak, gw ga akan ngebuat rasa sakit itu terulang kembali, Sil.\"")
    tekan_enter()
    clear_screen()
    print("Silvia: \"Yaudah ok ok... kalo lu ga bakal melakukan itu yaudah ok.\"")
    tekan_enter()
    clear_screen()
    print(f"{state.player_name}: \"Yaudah, trus gw juga udah ok, maksud gw kenapa lu?\"")
    tekan_enter()
    clear_screen()
    print("Silvia: \"Udah! Stop! Stop! Ya udah! Kan katanya lu baik. Ya udah. Kalau gitu diem di sini.\"")
    tekan_enter()
    clear_screen()
    print(f"{state.player_name}: \"Ya kenapa? Kenapa lu takut sama orang baik?\"")
    tekan_enter()
    clear_screen()
    print("Silvia: \"Lu itu hak gue. Kalau gue pengen pergi juga hak gue. Kenapa lu memaksakan kehendak gue?\"")
    tekan_enter()
    clear_screen()
    print(f"{state.player_name}: \"Tapi kan... Gue kan enggak jahat sama lu.\"")
    tekan_enter()
    clear_screen()
    print("Silvia: \"(tertawa sarkas) Lu enggak jahat? Lu udah berapa kali buat gw hancur. Tapi ya udah, kalo lu sekarang baik, bagus. Tapi rasa sakit yang gw rasain itu masih ada.\"")
    tekan_enter()
    clear_screen()
    print(f"{state.player_name}: \"Tapi-\"")
    tekan_enter()
    clear_screen()
    print("Silvia: \"Jadi ya udah, gue pengen pergi aja.\"")
    tekan_enter()
    clear_screen()
    print(f"{state.player_name}: \"Tapi kan gue pengen benerin itu semua. Gue sekarang pengen benerin itu semua.\"")
    tekan_enter()
    clear_screen()
    print("Silvia: \"Ga Bisa!\"")
    print(f"{state.player_name}: \"Bisa!\"")
    tekan_enter()
    clear_screen()
    print("Silvia: \"Ga Bisa! Ga Bisa!\"")
    print(f"{state.player_name}: \"Bisa! Bisa!\"")
    print("Silvia: \"Ga... ga bisa...\"")
    tekan_enter()
    clear_screen()
    print("\n Retakan itu sulit disatukan kembali. Kalian berpisah dengan banyak penyesalan.")
    print(" Waktu berlalu, namun luka itu tetap ada.")
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
        clear_screen()
        print("\nKamu memulai dengan pujian hangat.")
        print(f"\n{state.player_name} \"Malam ini kamu terlihat tenang. Aku senang bisa di sini.\" ")
        tekan_enter()
        clear_screen()
        print("Silvia: (tersenyum lembut) \"Iya... aku juga.\"")
        tekan_enter()
    elif pilihan3 == 2:
        state.affinity += 2
        clear_screen()
        print("\nKamu menceritakan masa sulit yang membuatmu berubah.")
        print(f"\n{state.player_name}: \"Dulu aku nggak pernah punya seseorang yang bisa diandalkan.\" ")
        print(f"{state.player_name}: \"Dulu aku sering merasa sendiri. Tapi setelah kenal kamu, aku merasa ada yang mendukung aku.\" ")
        tekan_enter()
        clear_screen()
        print(f"{state.player_name}: \"Makasih ya, udah ada buat aku.\" ")
        tekan_enter()
        clear_screen()
        print("Silvia: (mata berkaca) \"Aku juga... senang bisa ada buat kamu.\"")
        print("Silvia: \"Terima kasih sudah percaya sama aku.\" (mata berkaca)")
        tekan_enter()
    elif pilihan3 == 3:
        state.affinity -= 1
        clear_screen()
        print("\nKamu terlihat ragu, sering menunduk. Kesempatan terasa samar.")
        print("Silvia: \"Kamu kenapa? Ada yang mau kamu bilang?\" ")
        tekan_enter()
        clear_screen()
        print(f"{state.player_name}: \"Ah, nggak kok... aku cuma mikir aja.\" ")
        tekan_enter()
    else: # Option 4
        state.affinity -= 1
        clear_screen()
        print("\nKamu mulai bercanda berlebihan untuk mengalihkan perhatian.")
        print(f"{state.player_name}: \"Eh, kamu tau nggak? Kalo aku ini sebenarnya agen rahasia yang disuruh ngintip kamu.\" ")
        tekan_enter()
        clear_screen()
        print("Silvia: (tertawa canggung) \"Kamu ini... ?\" ")
        tekan_enter()
        clear_screen()
        print("\nKamu bercanda berlebihan. Silvia terlihat tidak yakin seberapa serius kamu.")
        tekan_enter()
        
    return True

def play_confession_scene(endings, state):
    # masih ada yang kurang sebelum bagian ini
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
        print("Silvia: \"Aku senang kita bisa tetap berteman.\"")
        tekan_enter()
        clear_screen()
        print("Kamu merasa lega, namun ada sedikit penyesalan.")
        print(f"Silvia: \"{state.player_name}, makasih ya. Kamu selalu ada.\"")
        tekan_enter()
        clear_screen()
        print(f"\n--- Ending tercapai: {endings[1].nama} [{endings[1].tipe}] ---")
        endings[1].tercapai = True
        tekan_enter()
        return False

    clear_screen()
    print("Kamu mengumpulkan keberanian dan mulai berbicara dari hati.")
    print("Silvia menatapmu dengan penuh perhatian.")
    print(f"{state.player_name}: \"Aku tidak akan bisa sampai sejauh ini tanpa kamu. Terima kasih ya.\"")
    tekan_enter()
    clear_screen()
    print("Silvia: \"Kenapa tiba-tiba lo? Lo bikin malu aja lo.\"")
    tekan_enter()
    clear_screen()
    print(f"{state.player_name}: \"Aku memang kayak gini. Aku nggak pernah punya seseorang yang kerja bareng dan saling dukung seperti ini.\"")
    print(f"{state.player_name}: \"Setelah kenal sama kamu, aku sadar aku nggak sebebas dulu. Aku berubah karena kehadiranmu.\"")
    tekan_enter()
    clear_screen()
    print("Silvia: \"Lo serius nih ngomongnya?\"")
    print("Silvia: \"Kenapa sih lo tiba-tiba ngomong gitu?\"")
    tekan_enter()
    clear_screen()
    print(f"{state.player_name}: \"Karena aku pengen jujur sama kamu. Aku suka kamu, Sil.\"")
    print(f"{state.player_name}: \"Maaf, agak terbawa suasana.\"")
    tekan_enter()
    clear_screen()
    print("Silvia: \"Aku juga... kadang merasa sendiri. Ada yang melindungi aku, ada yang aku lindungi. Tapi aku jarang menemukan yang seimbang.\"")
    print("Silvia: \"Saat aku ketemu kamu, aku sadar aku kesepian sebelumnya.\"")
    tekan_enter()

    clear_screen()
    if state.affinity >= 6:
        print("Silvia tersenyum, wajahnya memerah.")
        print("Silvia: \"Aku juga suka sama kamu, {state.player_name}. Aku senang kamu jujur.\"")
        tekan_enter()
        clear_screen()
        print("Silvia: \"T-Ta-Tapi aku pengen denger dulu, menurut kamu aku terlihat gimana malam ini?\"")
        tekan_enter()
        clear_screen()
        print(f"{state.player_name}: \"Malam ini kamu terlihat sangat cantik, Sil. Serius.\" ")
        tekan_enter()
        clear_screen()
        print("Silvia: (tersipu, canggung bahagia)")
        tekan_enter()
        clear_screen()
        print(f"{state.player_name}: \"Nah berarti gw ganteng apa nggak?\"")
        tekan_enter()
        clear_screen()
        print("Silvia: (tertawa kecil) \"Iya... iya... kamu juga ganteng kok.\"")
        tekan_enter()
        clear_screen()
        print("\nKamu berdua tertawa bersama, suasana menjadi hangat dan penuh harapan.")
        print("\n Malam itu menjadi awal yang baru. Kalian memulai hubungan dengan hangat.")
        print(f"\n--- Ending tercapai: {endings[0].nama} [{endings[0].tipe}] ---")
        endings[0].tercapai = True
    else:
        print("Silvia menunduk, suaranya lembut.")
        print("Silvia: \"Aku... aku nggak tahu harus bilang apa.\"")
        tekan_enter()
        clear_screen()
        print("Silvia terlihat bingung dan sedikit sedih.")
        print("Silvia: \"Aku butuh waktu untuk mikir... ini tiba-tiba banget buat aku.\"")
        print("Silvia: \"Aku nggak mau nyakitin perasaan kamu, tapi aku juga nggak yakin aku bisa balas perasaan itu.\"")
        tekan_enter()
        clear_screen()
        print("Kamu merasakan hatimu sedikit hancur, tapi kamu menghargai kejujurannya.")
        print(f"Silvia: \"{state.player_name}... maaf. Aku senang kamu jujur, tapi aku merasa kita lebih cocok sebagai teman.\"")
        print("Silvia: \"Kamu teman yang baik, {state.player_name}. Aku harap kita bisa tetap seperti ini.\"")
        tekan_enter()
        clear_screen()
        print("Kamu mengangguk, mencoba tersenyum meski hatimu berat.")
        print(f"{state.player_name}: \"Aku ngerti... kalau begitu aku akan tetap di sisimu sebagai teman.\"")
        tekan_enter()

        clear_screen()
        print("Malam itu berakhir dengan perasaan campur aduk, namun kamu menghargai kejujuran dan persahabatan kalian.")
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
    # Default Ending definitions
    default_ending_defs = [
        ("Heart Connected", "Happy Ending"),
        ("Unspoken Feelings", "True Ending"),
        ("Friendzone", "True Ending"),
        ("Broken Bonds", "Sad Ending"),
        ("Faded Away", "Sad Ending")
    ]
    
    # Load progress
    saved_name, saved_endings = load_progress()
    
    # Initialize endings list
    endings = []
    if saved_endings:
        # Restore state from save file
        for i, (nama, tipe) in enumerate(default_ending_defs):
            is_achieved = False
            # Check if we have data for this ending index
            if i < len(saved_endings):
                is_achieved = saved_endings[i].get("tercapai", False)
            endings.append(Ending(nama, tipe, is_achieved))
    else:
        # New game default
        for nama, tipe in default_ending_defs:
            endings.append(Ending(nama, tipe))

    # Initialize state with saved name (if any)
    state = GameState()
    state.player_name = saved_name

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
            # Allow user to enter new name or keep old one
            state.player_name = get_player_name(state.player_name, 50)
            play_story(endings, state)
            
            # Save progress after the story finishes
            save_progress(endings, state.player_name)
            
        elif menu == 2:
            show_endings(endings, state.player_name)
        elif menu == 3:
            clear_screen()
            print("Terima kasih telah bermain. Sampai jumpa.")
            tekan_enter()
            sys.exit()

if __name__ == "__main__":
    main()
