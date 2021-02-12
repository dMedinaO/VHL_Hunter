import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SurkeyVHLComponent } from './surkey-vhl.component';

describe('SurkeyVHLComponent', () => {
  let component: SurkeyVHLComponent;
  let fixture: ComponentFixture<SurkeyVHLComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SurkeyVHLComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SurkeyVHLComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
