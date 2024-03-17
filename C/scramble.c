#include<stdlib.h>
#include<stdio.h>
#include <stdio.h>
#include <stdint.h>

#define SLOW_CODE
#define PS_CODE

typedef uint32_t u32;
typedef uint16_t u16;
typedef uint8_t u8;

const u32 u32RandomIni[32] =
{
    0x0158001a, 0x441e9b63, 0xacc2f72e, 0x336386a5, 0xe36ca8e1, 0x851f8504, 0xa9dd54b8, 0x1b09a292,
    0x6be9836c, 0xe0071698, 0x09b13660, 0x00963742, 0x92605d74, 0x2019002e, 0x6a05d034, 0x3d57401f,
    0xb8cb5216, 0x00029840, 0x4a8801b9, 0x401f0052, 0xf8065020, 0x39179218, 0x00013001, 0xc8803121,
    0xca828f00, 0x7971001f, 0x004615c7, 0xd205694b, 0x1019006e, 0xb04a4f4c, 0x1d855bda, 0x00021290
};

// Get the seed
SLOW_CODE u32 FT_get_seed(u16 block, u16 pg, u8 ch, u8 ce) {
    u32 seed, rIni, shiftbit;

    seed = (block << 24) + (pg << 16) + (block << 8) + ((ce << 3) + (ch));
    rIni = pg % 28 + (((ce << 3) + (ch)) + block) % 5;
    shiftbit = pg % 32;
    seed = (seed << (shiftbit)) | (seed >> (32 - shiftbit)) | u32RandomIni[rIni];
    return seed;
}

// Scramble buffer data
PS_CODE void FT_scramble(u32 seed, void* buffer, u32 size) {
    u32* buf = (u32*)buffer;
    size = size >> 2; // u32 is 4 bytes
    while (size--) {
        // Scramble
        *buf = *buf ^ seed;
        buf++;
        // Update seed
        seed += 0x35ACCA53;
        seed = (seed << 1) | (seed >> 31);
    }
}
int main(int argc, char *argv[]) {
    if (argc < 4) {
        fprintf(stderr, "用example: %s <blk> <ch> <ce>\n", argv[0]);
        return 1;
    }

    FILE *fp;
    int blk, ch, ce;
    u32 *buffer;
    u32 size = 16384;
    buffer = (u32*)malloc(size * sizeof(u32));

    blk = atoi(argv[1]);
    ch = atoi(argv[2]);
    ce = atoi(argv[3]);

    for (u16 WL = 0; WL < 383; WL++) {
        for (u16 page = 0; page < 3; page++) {
            for (u32 i = 0; i < size / sizeof(u32); i++) {
                buffer[i] = 0xa5a5a5a5;
            }
            FT_scramble(FT_get_seed(blk, (WL * 3 + (page - 1)), ch, ce), buffer, size * sizeof(u32));
            fp = fopen("file.txt", "a");
            if (fp == NULL) {
                fprintf(stderr, "open err\n");
                return 1;
            }
            switch (page) {
                case 0:
                    fprintf(fp, "LSB\n");
                    break;
                case 1:
                    fprintf(fp, "CSB\n");
                    break;
                case 2:
                    fprintf(fp, "MSB\n");
                    break;
            }
            for (u32 i = 0; i < size / sizeof(u32); i++) {
                fprintf(fp, "%x ", buffer[i]);
            }
            fprintf(fp, "\n"); // 添加换行符
            fclose(fp);
        }
    }

    free(buffer); // 释放内存

    printf("success\n");

    return 0;
}