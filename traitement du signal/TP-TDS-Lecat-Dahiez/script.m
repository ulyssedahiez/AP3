clear all
close all

%Question 1A : 

X = zeros(512, 512);

for x=206:306 
    for y=206:306  
        X(x,y) = 255;
    end
end

figure
colormap(gray(64));
imshow(X)

%Question 2B et 2C
Dct = dct2(X);


m2 = Dct(:);
pct80=round(512*512*0.8);
pct50=round(512*512*0.5);
pct20=round(512*512*0.2);

Dcts = sort(m2,'descend');
Dct(abs(Dct) < Dcts(pct20)) = 0;

figure
colormap(gray(64));
plot(Dcts)


figure
colormap(gray(64));
imshow(idct2(Dct));


% Exercice 2 

%Question 2b

image1 = imread("image1.ascii.pgm");
figure
colormap(gray(64));
imshow(image1);
%Question 2c

Dctimage = dct2(image1);

m2image = Dctimage(:);
pctimage=round(512*512*0.005);

Dctsimage = sort(m2image,'descend');
Dctimage(abs(Dctimage) < Dctsimage(pctimage)) = 0;

%figure
figure
colormap(gray(64));
image(idct2(Dctimage),'cdatamapping','scaled')


%dct80 = reshape(dct, [], round(0.2*512), 1);

%I = image(Dcts,'cdatamapping','scaled');

%Question 2D





%set(gca,'clim',[28 33]);