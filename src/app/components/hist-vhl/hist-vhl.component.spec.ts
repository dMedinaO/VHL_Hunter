import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HistVHLComponent } from './hist-vhl.component';

describe('HistVHLComponent', () => {
  let component: HistVHLComponent;
  let fixture: ComponentFixture<HistVHLComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HistVHLComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HistVHLComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
