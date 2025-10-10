#include <stdio.h>


	int pilihan ;

    char hasilPilihFilm [10][50] = {};

    char hariYangDipilih [10][50] = {};

    char pemilihanFilm [][50] = {"spiderman", "conjuring","IT"};

    char weekdays [][50] = {"senin", "selasa", "rabu", "kamis", "jumat",};

    char weekend [][50] = {"sabtu", "minggu"};

    double harga [] = {40, 50};

    char posisiDuduk [][50] = {"bawah", "tengah", "atas"};

    char metodePembayaran [][50] = {"cashless" , "cash"};



int milihHari () {
    printf("weekdays : \n");
    for (int i = 0; i < 5; i++)
    {
        /* code */
        printf("%d. %s\n", i + 1, weekdays[i]);
    }
    printf("weekend : \n");
    for (int i = 0; i < 2; i++)
    {
        /* code */
        printf("%d. %s\n", i+1, weekend[i]);
    }
    
    
    printf("PIlih hari : ");
    scanf("%s", &hariYangDipilih);

    return 0;
}

int milihPosisiDuduk () {
    printf("pilih posisi duduk : \n");
    for (int i = 0; i < 3; i++)
    {
        /* code */
        printf("%d. %s\n", i + 1, posisiDuduk[i]);
    }
    printf("masukan pilihan : ");
    scanf("%s", &posisiDuduk);

    return 0;
}


int main () {
    
    printf("\n=== Pilihan Film ===\n");
    for (int i = 0; i < 3; i++) {
        printf("%d. %s\n", i + 1, pemilihanFilm[i]);
    }
    printf("Masukkan pilihan Anda (1-3): ");
    
    scanf("%d", &pilihan);

    if (pilihan < 1 || pilihan > 3) {
        printf("Pilihan tidak valid. Silakan coba lagi.\n");
    }

    switch (pilihan)
    {
    case 1:
        printf("Anda memilih film %s\n", pemilihanFilm[0]);
        milihHari();
        milihPosisiDuduk();
        printf("harga tiketnya adalah : %.2f\n", harga[0]);

        break;
    
    default:
        printf("Pilihan tidak valid. Silakan coba lagi.\n");
        break;
    }
    
    

    return 0;

}
