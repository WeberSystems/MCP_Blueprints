// Fill out your copyright notice in the Description page of Project Settings.


#include "MCPTestCharacter.h"

// Sets default values
AMCPTestCharacter::AMCPTestCharacter()
{
 	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

}

// Called when the game starts or when spawned
void AMCPTestCharacter::BeginPlay()
{
	Super::BeginPlay();
	
}

// Called every frame
void AMCPTestCharacter::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}

// Called to bind functionality to input
void AMCPTestCharacter::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
	Super::SetupPlayerInputComponent(PlayerInputComponent);

}

