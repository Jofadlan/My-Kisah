#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_ENDING 5
#define MAX_NAMA 50
#define MAX_STR 120

typedef struct {
    char nama[MAX_STR];
    char tipe[MAX_STR];
    bool tercapai;
} Ending;

// Fungsi untuk membersihkan layar 
void clearScreen() {
    system("cls");
}

// Fungsi untuk menunggu input Enter
void tekanEnter() {
    printf("\n( Tekan Enter untuk melanjutkan )");
    getchar();
}

// Fungsi untuk validasi input numerik
int getValidInput(int min, int max) {
    int choice;
    while (scanf("%d", &choice) != 1 || choice < min || choice > max) {
        printf("Pilihan tidak valid. \nMasukkan angka diantara %d - %d: ", min, max);
        while (getchar() != '\n');
    }
    getchar();
    return choice;
}

// Fungsi untuk validasi nama pemain
void getPlayerName(char playerName[], int maxLength) {
    printf("Masukkan nama karaktermu: ");
    fgets(playerName, maxLength, stdin);
    playerName[strcspn(playerName, "\n")] = '\0';
    while (strlen(playerName) == 0) {
        printf("Nama tidak boleh kosong. \nMasukkan nama: ");
        fgets(playerName, maxLength, stdin);
        playerName[strcspn(playerName, "\n")] = '\0';
    }
}

// Fungsi untuk menampilkan riwayat ending
void showEndings(Ending endings[], int size) {
    clearScreen();
    printf("=== RIWAYAT ENDING ===\n\n");
    bool ada = false;
    for (int i = 0; i < size; i++) {
        if (endings[i].tercapai) {
            printf(" %s [%s]\n", endings[i].nama, endings[i].tipe);
            ada = true;
        }
    }
    if (!ada) {
        printf("Belum ada ending yang tercapai.\n");
    }
    tekanEnter();
}

// Scene 1: Pertemuan di kafe
bool playCafeScene(Ending endings[], char playerName[], int *affinity) {
    clearScreen();
    printf(" Malam itu kalian bertemu lagi di kafe langganan.\n");
    printf(" %s, dan Silvia sudah lama saling kenal-namun belakangan ada sesuatu yang menggantung.\n", playerName);
    tekanEnter();

    clearScreen();
    printf("Kamu melihat Silvia di pojok kafe. Dia tampak sendirian.\n");
    printf("Apa yang akan kamu lakukan?\n");
    printf("1. Datang dan sapa dengan hangat.\n");
    printf("2. Duduk pelan di sampingnya, menunggu suasana santai.\n");
    printf("3. Menunggu sampai dia memperhatikanmu lalu menyapa.\n");
    printf("4. Terlihat gugup dan pergi dari kafe.\n");
    printf("5. Kembali ke menu utama.\n");
    printf("Pilih: ");

    int pilihan1 = getValidInput(1, 5);
    if (pilihan1 == 5) return false; // Kembali ke menu utama

    if (pilihan1 == 4) {
        clearScreen();
        printf("Kamu: (terlalu gugup, kamu memutuskan pergi tanpa bicara.)\n");
        printf(" Hari-hari berikutnya komunikasi memudar. Silvia mulai menjauh.\n");
        printf("\n--- Ending tercapai: %s [%s] ---\n", endings[4].nama, endings[4].tipe);
        endings[4].tercapai = true;
        tekanEnter();
        return false; // Cerita berakhir
    } else if (pilihan1 == 1) {
        *affinity += 2;
        printf("\nKamu mendekat dan menyapa dengan tenang.\n");
        printf("Silvia: \"Oh, hai. Senang kamu mampir.\" (senyum tipis)\n");
        tekanEnter();
    } else if (pilihan1 == 2) {
        *affinity += 2;
        printf("\nKamu duduk perlahan di sampingnya, memberi ruang.\n");
        printf("Silvia: \"Kamu baik-baik saja?\" (suara lembut)\n");
        tekanEnter();
    } else {
        printf("\nKamu menunggu momen. Saat dia menoleh, kamu tersenyum.\n");
        printf("Silvia: \"Oh, akhirnya kamu datang juga.\" (pelan)\n");
        tekanEnter();
    }
    return true; // Lanjut ke scene berikutnya
}

// Scene 2: Percakapan awal
bool playConversationScene(Ending endings[], char playerName[], int *affinity, bool *conflictFlag, bool *brokenBondFlag) {
    clearScreen();
    printf("Kalian mulai berbincang. Pilih bagaimana gaya bicaramu.\n");
    printf("1. Cerita ringan tentang kerja / kegiatan.\n");
    printf("2. Tanyakan bagaimana perasaannya akhir-akhir ini.\n");
    printf("3. Goda dengan bercanda.\n");
    printf("4. Menyinggung hal yang sensitif di masa lalu.\n");
    printf("5. Kembali ke menu utama.\n");
    printf("Pilih: ");

    int pilihan2 = getValidInput(1, 5);
    if (pilihan2 == 5) return false;

    if (pilihan2 == 1) {
        *affinity += 2;
        printf("\nKamu: \"Kerjaan belakangan gimana?\" \n");
        printf("Silvia: \"Lumayan sibuk, tapi senang ada yang nemenin.\" (tersenyum)\n");
        tekanEnter();
    } else if (pilihan2 == 2) {
        *affinity += 1;
        printf("\nKamu menanyakan hal personal dengan hati-hati.\n");
        printf("Silvia: \"Kadang capek, tapi aku baik kok. Makasih udah nanya.\" \n");
        tekanEnter();
    } else if (pilihan2 == 3) {
        *affinity += 1;
        printf("\nKamu menggoda Silvia soal minuman yang dia pesan.\n");
        printf("Silvia: (tersipu) \"Dasar.\", namun terlihat hangat.\n");
        tekanEnter();
    } else {
        *affinity -= 3;
        *conflictFlag = true;
        printf("\nKamu menyentuh topik lama yang jelas menyakitinya.\n");
        printf("Silvia: \"Kenapa kamu harus bawa itu lagi?\" Suaranya meninggi.\n");
        tekanEnter();

        clearScreen();
        printf("Percakapan memanas. Pilih responsmu:\n");
        printf("1. Minta maaf dan tarik kata-katamu.\n");
        printf("2. Tetap bersikap defensif dan membela dirimu.\n");
        printf("3. Coba ubah topik dan bersikap tenang.\n");
        printf("4. Kembali ke menu utama.\n");
        printf("Pilih: ");
        int pilihan_conflict = getValidInput(1, 4);
        if (pilihan_conflict == 4) return false;

        if (pilihan_conflict == 1) {
            *affinity += 1;
            *conflictFlag = false;
            printf("\nKamu: \"Maaf, aku keterusan. Aku nggak bermaksud nyakitin.\" \n");
            printf("Silvia: (menarik napas) \"Ya udah... kita lanjut aja.\"\n");
            tekanEnter();
        } else if (pilihan_conflict == 2) {
            *affinity -= 2;
            *conflictFlag = true;
            *brokenBondFlag = true;
            printf("\nKamu bersikap defensif. Silvia terlihat sangat terluka dan berdiri.\n");
            printf("Silvia: \"Aku butuh waktu.\" (lalu pergi dari meja)\n");
            tekanEnter();
        } else {
            printf("\nKamu mencoba meredam suasana dengan hati-hati.\n");
            printf("Silvia: \"Baiklah... kita bicara lain kali.\" (nada dingin)\n");
            tekanEnter();
        }
    }
    return true;
}

// Scene 3: Konflik (Broken Bonds)
bool playConflictScene(Ending endings[], char playerName[], int *affinity) {
    clearScreen();
    printf("Beberapa hari setelah kejadian di kafe, suasana benar-benar berubah.\n");
    printf("Kalian tetap bertemu beberapa kali, namun ada jarak yang tak hilang.\n");
    printf(" Suatu malam kalian akhirnya bertemu untuk bicara satu kali lagi.\n");
    tekanEnter();

    clearScreen();
    printf("%s: \"Yaudah ya, kenapa lu menjauh?\"\n", playerName);
    printf("Silvia: \"Gw ga menjauh, gw ga menjauh.\"\n");
    printf("%s: \"Yaudah...\"\n", playerName);
    printf("Silvia: \"Melihat dari apa-apa yang sudah lalu aja, gw ga mau nyakitin diri gw sendiri.\"\n");
    printf("%s: \"Nggak, gw udah nggak kayak dulu lagi. Gw udah berubah.\"\n", playerName);
    printf("Silvia: \"Ok kalo lu udah berubah, bagus. Tapi rasa sakit yang gue rasain dulu masih ada.\"\n");
    printf("%s: \"Nggak, gw ga akan ngebuat rasa sakit itu terulang kembali, Sil.\"\n", playerName);
    printf("Silvia: \"Yaudah ok ok... kalo lu ga bakal melakukan itu yaudah ok.\"\n");
    printf("%s: \"Yaudah, trus gw juga udah ok, maksud gw kenapa lu?\"\n", playerName);
    printf("Silvia: \"Udah! Stop! Stop! Ya udah! Kan katanya lu baik. Ya udah. Kalau gitu diem di sini.\"\n");
    printf("%s: \"Ya kenapa? Kenapa lu takut sama orang baik?\"\n", playerName);
    printf("Silvia: \"Lu itu hak gue. Kalau gue pengen pergi juga hak gue. Kenapa lu memaksakan kehendak gue?\"\n");
    printf("%s: \"Tapi kan... Gue kan enggak jahat sama lu.\"\n", playerName);
    printf("Silvia: \"(tertawa sarkas) Lu enggak jahat? Lu udah berapa kali buat gw hancur. Tapi ya udah, kalo lu sekarang baik, bagus. Tapi rasa sakit yang gw rasain itu masih ada.\"\n");
    printf("%s: \"Tapi-\"\n", playerName);
    printf("Silvia: \"Jadi ya udah, gue pengen pergi aja.\"\n");
    printf("%s: \"Tapi kan gue pengen benerin itu semua. Gue sekarang pengen benerin itu semua.\"\n", playerName);
    printf("Silvia: \"Ga Bisa!\"\n");
    printf("%s: \"Bisa!\"\n", playerName);
    printf("Silvia: \"Ga Bisa! Ga Bisa!\"\n");
    printf("%s: \"Bisa! Bisa!\"\n", playerName);
    printf("Silvia: \"Ga... ga bisa...\"\n");
    printf("\n Retakan itu sulit disatukan kembali. Kalian berpisah dengan banyak penyesalan.\n");
    printf("\n--- Ending tercapai: %s [%s] ---\n", endings[3].nama, endings[3].tipe);
    endings[3].tercapai = true;
    tekanEnter();
    return false;
}

// Scene 4: Momen jujur
bool playHonestMomentScene(Ending endings[], char playerName[], int *affinity) {
    clearScreen();
    printf("Momen tenang muncul. Kamu rasakan kesempatan untuk lebih jujur.\n");
    printf("Pilih cara kamu mempersiapkan diri sebelum mengatakannya:\n");
    printf("1. Rangkul kehangatan suasana, mulai dengan pujian sederhana.\n");
    printf("2. Ceritakan sesuatu yang rentan dari dirimu dulu.\n");
    printf("3. Terlihat ragu dan sering terdiam.\n");
    printf("4. Bercanda berlebihan untuk menutupi perasaan.\n");
    printf("5. Kembali ke menu utama.\n");
    printf("Pilih: ");

    int pilihan3 = getValidInput(1, 5);
    if (pilihan3 == 5) return false;

    if (pilihan3 == 1) {
        *affinity += 3;
        printf("\nKamu: \"Malam ini kamu terlihat tenang. Aku senang bisa di sini.\" \n");
        printf("Silvia: (tersenyum lembut) \"Iya... aku juga.\"\n");
        tekanEnter();
    } else if (pilihan3 == 2) {
        *affinity += 2;
        printf("\nKamu menceritakan masa sulit yang membuatmu berubah.\n");
        printf("Silvia: \"Terima kasih sudah percaya sama aku.\" (mata berkaca)\n");
        tekanEnter();
    } else if (pilihan3 == 3) {
        *affinity -= 1;
        printf("\nKamu terlihat ragu, sering menunduk. Kesempatan terasa samar.\n");
        tekanEnter();
    } else {
        *affinity -= 1;
        printf("\nKamu bercanda berlebihan. Silvia terlihat tidak yakin seberapa serius kamu.\n");
        tekanEnter();
    }
    return true;
}

// Confession
bool playConfessionScene(Ending endings[], char playerName[], int *affinity) {
    clearScreen();
    printf("Sekarang momen itu datang. Apakah kamu akan menyatakan perasaanmu?\n");
    printf("1. Ya\n");
    printf("2. Tidak\n");
    printf("3. Kembali ke menu utama.\n");
    printf("Pilih: ");

    int pilih_confess = getValidInput(1, 3);
    if (pilih_confess == 3) return false;

    if (pilih_confess == 2) {
        clearScreen();
        printf("Kamu memutuskan untuk tidak mengatakannya. Hubungan tetap sebagai teman.\n");
        printf("Silvia: \"%s, makasih ya. Kamu selalu ada.\"\n", playerName);
        printf("\n--- Ending tercapai: %s [%s] ---\n", endings[1].nama, endings[1].tipe);
        endings[1].tercapai = true;
        tekanEnter();
        return false;
    }

    clearScreen();
    printf("%s: \"Aku tidak akan bisa sampai sejauh ini tanpa kamu. Terima kasih ya.\"\n", playerName);
    printf("Silvia: \"Kenapa tiba-tiba lo? Lo bikin malu aja lo.\"\n");
    printf("%s: \"Aku memang kayak gini. Aku nggak pernah punya seseorang yang kerja bareng dan saling dukung seperti ini.\"\n", playerName);
    printf("%s: \"Setelah kenal sama kamu, aku sadar aku nggak sebebas dulu. Aku berubah karena kehadiranmu.\"\n", playerName);
    printf("Silvia: \"Kenapa sih lo tiba-tiba ngomong gitu?\"\n");
    printf("%s: \"Maaf, agak terbawa suasana.\"\n", playerName);
    printf("Silvia: \"Aku juga... kadang merasa sendiri. Ada yang melindungi aku, ada yang aku lindungi. Tapi aku jarang menemukan yang seimbang.\"\n");
    printf("Silvia: \"Saat aku ketemu kamu, aku sadar aku kesepian sebelumnya.\"\n");
    tekanEnter();

    clearScreen();
    if (*affinity >= 7) {
        printf("Silvia tersenyum, wajahnya memerah.\n");
        printf("Silvia: \"T-Ta-Tapi gue pengen denger dulu, menurut lo ini gue terlihat gimana malam ini?\"\n");
        printf("%s: \"Malam ini lo terlihat sangat cantik, Sil. Serius.\" \n", playerName);
        printf("Silvia: (tersipu, canggung bahagia)\n");
        printf("%s: \"Nah berarti gue ganteng apa nggak?\"\n", playerName);
        printf("Silvia: \"Iya... Iya bang... iya kok iya.\"\n");
        printf("\n Malam itu menjadi awal yang baru. Kalian memulai hubungan dengan hangat.\n");
        printf("\n--- Ending tercapai: %s [%s] ---\n", endings[0].nama, endings[0].tipe);
        endings[0].tercapai = true;
    } else {
        printf("Silvia menunduk, suaranya lembut.\n");
        printf("Silvia: \"%s... maaf. Aku senang kamu jujur, tapi aku merasa kita lebih cocok sebagai teman.\"\n", playerName);
        printf("%s: \"Aku ngerti... kalau begitu aku akan tetap di sisimu sebagai teman.\"\n", playerName);
        printf("\n--- Ending tercapai: %s [%s] ---\n", endings[2].nama, endings[2].tipe);
        endings[2].tercapai = true;
    }
    tekanEnter();
    return false;
}

void playStory(Ending endings[], char playerName[]) {
    int affinity = 0;
    bool conflictFlag = false;
    bool brokenBondFlag = false;

    if (!playCafeScene(endings, playerName, &affinity)) return;
    if (!playConversationScene(endings, playerName, &affinity, &conflictFlag, &brokenBondFlag)) return;
    if (brokenBondFlag) {
        playConflictScene(endings, playerName, &affinity);
        return;
    }
    if (!playHonestMomentScene(endings, playerName, &affinity)) return;
    playConfessionScene(endings, playerName, &affinity);
}

int main() {
    Ending endings[MAX_ENDING] = {
        {"Heart Connected", "Happy Ending", false},
        {"Unspoken Feelings", "True Ending", false},
        {"Friendzone", "True Ending", false},
        {"Broken Bonds", "Sad Ending", false},
        {"Faded Away", "Sad Ending", false}
    };

    int menu = 0;
    char playerName[MAX_NAMA] = "";

    do {
        clearScreen();
        printf("====================\n");
        printf("   \"My Kisah\" \n");
        printf("====================\n");
        printf("1. Main Cerita\n");
        printf("2. Lihat Riwayat Ending\n");
        printf("3. Keluar\n");
        printf("Pilih menu: ");
        menu = getValidInput(1, 3);

        switch (menu) {
            case 1:
                getPlayerName(playerName, MAX_NAMA);
                playStory(endings, playerName);
                break;

            case 2:
                showEndings(endings, MAX_ENDING);
                break;

            case 3:
                clearScreen();
                printf("Terima kasih telah bermain. Sampai jumpa.\n");
                tekanEnter();
                break;
        }
    } while (menu != 3);

    return 0;
}
